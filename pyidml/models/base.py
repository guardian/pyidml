import mongoengine
from pyidml.fields import *

class XMLSerializableMixin(object):
    @classmethod
    def from_xml(cls, e):
        data = {}
        
        for attr, value in e.items():
            if attr in cls._fields:
                data[attr] = cls._fields[attr].to_python(value)
        for child in e:
            # If we have specifically defined a field for this child element, 
            # use that
            if child.tag in cls._fields:
                data[child.tag] = cls._fields[child.tag].to_python(child)
            # Otherwise, try to magically add it to self.children by finding 
            # the right subclass of Element
            else:
                subclasses = Element._get_subclasses()
                subclass_name = 'Element.' + child.tag
                if subclass_name in subclasses:
                    if 'children' not in data:
                        data['children'] = []
                    data['children'].append(
                        subclasses[subclass_name].from_xml(child)
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


class Properties(Element):
    Label = KeyValuePairField()
