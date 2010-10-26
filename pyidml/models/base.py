import mongoengine
import numpy
from pyidml.fields import *
import sys

class XMLSerializableMixin(object):
    @classmethod
    def from_xml(cls, e):
        """
        Returns an instance of this class for the given XML element.
        """
        data = {}
        subclass_tags = Element._get_subclass_tags()
        
        for attr, value in e.items():
            # TODO: A KeyError may want to be supressed here for production
            try:
                data[attr] = cls._fields[attr].to_python(value)
            except:
                exc_class, exc, tb = sys.exc_info()
                new_exc = Exception('%s (%s in %s)'
                                    % (exc or exc_class, attr, cls))
                raise exc_class, new_exc, tb
            
            
        for child in e:
            # If we have specifically defined a field for this child element, 
            # use that
            if child.tag in cls._fields:
                data[child.tag] = cls._fields[child.tag].to_python(child)
            # Otherwise, try to magically add it to self.children by finding 
            # the right subclass of Element
            else:
                if child.tag in subclass_tags:
                    if 'children' not in data:
                        data['children'] = []
                    data['children'].append(
                        subclass_tags[child.tag].from_xml(child)
                    )
        
        return cls(**data)
    

class ElementEmbeddedDocumentField(EmbeddedDocumentField):
    """
    Hack for a self-referential EmbeddedDocumentField in a ListField
    """
    def __init__(self, **kwargs):
        super(mongoengine.EmbeddedDocumentField, self).__init__(**kwargs)
    
    @property
    def document(self):
        return Element
    

class ElementMixin(object):
    def get_children(self, name):
        """
        Returns a list of children with of a given element name.
        """
        if not self.children:
            return []
        return filter(lambda c: c.__class__.__name__ == name, self.children)
   
    def get_element(self, name):
        """
        Returns the child with the given element ID.
        """
        if not self.children:
            return None
        for child in self.children:
            if getattr(child, 'Self', None) == name:
                return child

    def get_document(self):
        """
        Get the root element for the current document.
        """
        if self._class_name == 'Document':
            return self
        elif getattr(self, '_parent', None) is not None:
            return self._parent.get_document()
    
    def get_transform(self, name=None):
        """
        Returns the transform matrix for this element relative to the nearest 
        element of the given name, or by default, the pasteboard.
        """
        if self.__class__.__name__ == name:
            return numpy.identity(3)
        if hasattr(self, 'ItemTransform'):
            transformation = numpy.matrix([
                [self.ItemTransform[0], self.ItemTransform[1], 0],
                [self.ItemTransform[2], self.ItemTransform[3], 0],
                [self.ItemTransform[4], self.ItemTransform[5], 1],
            ])
        else:
            transformation = numpy.identity(3)
        if hasattr(self, '_parent') and self._parent:
            return transformation * self._parent.get_transform(name)
        else:
            return transformation


    def transform_coordinates(self, coords):
        """
        Returns coordinates relative to the spread given coordinates relative to 
        this element.
        """
        coords_matrix = numpy.matrix([coords[0], coords[1], 1])
        result = coords_matrix * self.get_spread_transform()
        return (result[0, 0], result[0, 1])
        
    

class Element(mongoengine.EmbeddedDocument, XMLSerializableMixin, ElementMixin):
    children = ListField(ElementEmbeddedDocumentField())
    
    @classmethod
    def _get_subclasses(cls):
        try:
            return cls._subclasses
        except AttributeError:
            cls._subclasses = super(Element, cls)._get_subclasses()
            return cls._subclasses
    
    @classmethod
    def _get_subclass_tags(cls):
        try:
            return cls._subclass_tags
        except AttributeError:
            cls._subclass_tags = dict([
                (k.split('.')[-1], v)
                for k, v in cls._get_subclasses().items()
            ])
            return cls._subclass_tags
        
    

class Properties(Element):
    Label = KeyValuePairField()
    
