import mongoengine
from mongoengine.base import BaseDocument
from xml.etree import ElementTree

IntField = mongoengine.IntField

class StringField(mongoengine.StringField):
    def to_python(self, value):
        if isinstance(value, ElementTree._ElementInterface):
            value = value.text
        return super(StringField, self).to_python(value)
    

class FloatField(mongoengine.FloatField):
    def to_python(self, value):
        if isinstance(value, ElementTree._ElementInterface):
            value = value.text
        return super(FloatField, self).to_python(value)
    

class BooleanField(mongoengine.BooleanField):
    def to_python(self, value):
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
        if isinstance(value, ElementTree._ElementInterface):
            return self.document.from_xml(value)
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
        if isinstance(value, ElementTree._ElementInterface):
            d = {}
            for child in value:
                d[child.get('Key')] = child.get('Value')
            return d
        return super(KeyValuePairField, self).to_python(value)

class PropertiesField(mongoengine.DictField):
    def to_python(self, value):
        if isinstance(value, ElementTree._ElementInterface):
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
        if isinstance(value, ElementTree._ElementInterface):
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


