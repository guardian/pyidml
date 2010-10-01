import mongoengine
from xml.etree import ElementTree

IntField = mongoengine.IntField
FloatField = mongoengine.FloatField
ListField = mongoengine.ListField


class StringField(mongoengine.StringField):
    def to_python(self, value):
        if isinstance(value, ElementTree._ElementInterface):
            value = value.text
        return super(StringField, self).to_python(value)
    

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
    

class SpaceSeparatedListField(mongoengine.ListField):
    def to_python(self, value):
        if isinstance(value, basestring):
            value = value.split()
        return super(SpaceSeparatedListField, self).to_python(value)
    
    def to_xml(self, value):
        return ' '.join(unicode(v) for v in super(SpaceSeparatedListField, self).to_xml(value))
    

class EmbeddedDocumentField(mongoengine.EmbeddedDocumentField):
    def to_python(self, value):
        if isinstance(value, ElementTree._ElementInterface):
            return self.document.from_xml(value)
        return super(EmbeddedDocumentField, self).to_python(value)

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

