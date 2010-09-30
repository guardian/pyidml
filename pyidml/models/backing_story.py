from pyidml.fields import *
from pyidml.models import Element, Properties
from stories import Story

class BackingStory(Element):
    """
    The BackingStory.xml file in an IDML package contains any XML content in the 
    XML structure of the InDesign document that has not been placed in the 
    layout.
    """
    DOMVersion = StringField(required=True)
    

class XMLStory(Story):
    """
    An <XMLStory> element represents XML text content that has not yet been 
    placed in a layout.
    
    The <XMLStory> element is identical to the <Story> element.
    """
    

class XMLElement(Element):
    """
    The <XMLElement> elements in an IDML file represent XML content in the 
    structure of an InDesign document.
    """
    Self = StringField(required=True)
    MarkupTag = StringField()
    XMLContent = StringField()
    NoTextMarker = BooleanField()
    

class XMLAttribute(Element):
    Name = StringField(required=True)
    Value = StringField(required=True)
    

class XMLInstruction(Element):
    StoryOffset = StringField()
    Target = StringField(required=True)
    Data = StringField()
    

class XMLComment(Element):
    Self = StringField(required=True)
    Value = StringField()
    

class DTDProperties(Properties):
    Contents = StringField()
    

class DTD(Element):
    Self = StringField(required=True)
    
    Properties = EmbeddedDocumentField(DTDProperties)
    

# TODO: XMLExportMap, XMLImportMap, XMLTag, 

