import mongoengine
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
        if not self.children:
            return []
        return filter(lambda c: c.__class__.__name__ == name, self.children)
    

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
    
