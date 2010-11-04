from pyidml.fields import *
from pyidml.models import Element, Properties

class Tags(Element):
    DOMVersion = StringField()

class XMLTagProperties(Properties):
    TagColor = StringField() # TODO InDesignUIColorType_TypeDef
    

class XMLTag(Element):
    Self = StringField(required=True)
    Name = StringField(required=True)
    
    Properties = EmbeddedDocumentField(XMLTagProperties)
    

