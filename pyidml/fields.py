import mongoengine
from mongoengine.base import BaseDocument, BaseField
from lxml import etree

IntField = mongoengine.IntField

class StringField(mongoengine.StringField):
    def to_python(self, value):
        if isinstance(value, etree._Element):
            value = value.text
        return super(StringField, self).to_python(value)
    

class FloatField(mongoengine.FloatField):
    def to_python(self, value):
        if isinstance(value, etree._Element):
            value = value.text
        return super(FloatField, self).to_python(value)
    

class BooleanField(mongoengine.BooleanField):
    def to_python(self, value):
        if isinstance(value, etree._Element):
            value = value.text
        if isinstance(value, basestring):
            if value == 'true' or value == '1':
                return True
            else:
                return False
        return super(BooleanField, self).to_python(value)
    
    def to_xml(self, value):
        if value:
            return 'true'
        else:
            return 'false'
    

class ListField(mongoengine.ListField):
    """
    A ListField which passes through _parent references to 
    EmbeddedDocumentFields
    """
    def _set_parent(self, instance, value):
        if isinstance(self.field, EmbeddedDocumentField) and value is not None:
            for doc in value:
                if isinstance(doc, BaseDocument):
                    doc._parent = instance
        
    def __set__(self, instance, value):
        self._set_parent(instance, value)
        super(ListField, self).__set__(instance, value)
    
    def __get__(self, instance, owner):
        value = super(ListField, self).__get__(instance, owner)
        self._set_parent(instance, value)
        return value
    

class ListItemField(ListField):
    def __get__(self, instance, owner):
        value = super(ListItemField, self).__get__(instance, owner)
        if value == []:
            return None
        return value

class SpaceSeparatedListField(ListField):
    def to_python(self, value):
        if isinstance(value, basestring):
            value = value.split()
        return super(SpaceSeparatedListField, self).to_python(value)
    
    def to_xml(self, value):
        return ' '.join(
            unicode(v) for v in 
            super(SpaceSeparatedListField, self).to_xml(value)
        )
    

class EmbeddedDocumentField(mongoengine.EmbeddedDocumentField):
    """
    An EmbeddedDocumentField that can deserialize from XML elements and gives
    values a _parent attribute
    """
    def to_python(self, value):
        if isinstance(value, etree._Element):
            return self.document_type.from_xml(value)
        return super(EmbeddedDocumentField, self).to_python(value)
    
    def __set__(self, instance, value):
        if isinstance(value, BaseDocument):
            value._parent = instance
        super(EmbeddedDocumentField, self).__set__(instance, value)
    
    def __get__(self, instance, owner):
        value = super(EmbeddedDocumentField, self).__get__(instance, owner)
        if isinstance(value, BaseDocument):
            value._parent = instance
        return value
    

class KeyValuePairField(mongoengine.DictField):
    def to_python(self, value):
        if isinstance(value, etree._Element):
            d = {}
            for child in value:
                d[child.get('Key')] = child.get('Value')
            return d
        return super(KeyValuePairField, self).to_python(value)

class PropertiesField(mongoengine.DictField):
    def to_python(self, value):
        if isinstance(value, etree._Element):
            d = {}
            for child in value:
                attrs = dict(child.items())
                if attrs:
                    d['attrs'] = attrs
                if len(child) == 0:
                    d[child.tag] = child.text
                else:
                    d[child.tag] = self.to_python(child)
            return d
        return super(PropertiesField, self).to_python(value)
    

class RectangleBoundsField(mongoengine.DictField):
    def to_python(self, value):
        if isinstance(value, etree._Element):
            d = {}
            for attr in ('Top', 'Left', 'Bottom', 'Right'):
                d[attr] = float(value.get(attr))
            return d
        return super(RectangleBoundsField, self).to_python(value)

# class StyleField(StringField):
#     def to_python(self, value):
#         value = super(StyleField, self).to_python(value)
#         styles = self.owner_document.get_document().get_children('Styles')[0]
#         return styles.get_style(value)
#     
#     def to_mongo(self, value):
#         return value.Self
#     

class ObjectReferenceField(StringField):
    """
    A reference to another element in an InDesign document which will be 
    automatically dereferenced on access.

    On creation, it is passed a string specifying the parent element to look for 
    the referenced element under, relative to the root document. For example, 
    references to ParagraphStyle elements would have a parent of 
    ``Styles/RootParagraphStyleGroup``.
    """
    def __init__(self, parent_element='', **kwargs):
        self.parent_element = parent_element
        super(ObjectReferenceField, self).__init__(**kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            # Document class
            return self
        
        value = instance._data.get(self.name)
        if isinstance(value, basestring):
            parent = instance.get_document()
            for element_name in self.parent_element.split('/'):
                if element_name == '':
                    continue
                parent = getattr(parent, element_name, None)
            if parent is not None:
                element = parent.get_element(value)
                if element is not None:
                    instance._data[self.name] = element
        return super(ObjectReferenceField, self).__get__(instance, owner)

    def to_mongo(self, element):
        if isinstance(element, BaseDocument):
            element = element.Self
        return element

    def prepare_query_value(self, op, value):
        return self.to_mongo(value)




