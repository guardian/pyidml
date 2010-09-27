from pyidml.fields import *
from pyidml.models import Element, Properties

class Fonts(Element):
    """
    Defines the fonts and composite fonts used in a document.
    
    Even an empty InDesign document contains references to default fonts and 
    composite fonts.
    """
    DOMVersion = StringField(required=True)
    

class FontFamily(Element):
    """
    A font family is a group of similar fonts.
    
    For example, the fonts "Arial Regular", "Arial Bold", and "Arial Italic" all 
    belong to the same font family. A <FontFamily> element groups together 
    <Font> elements, and each <Font> element defines a specific font.
    """
    Self = StringField(required=True)
    Name = StringField()
    

class Font(Element):
    """
    Defines a specific font.
    """
    Self = StringField(required=True)
    FontFamily = StringField()
    Name = StringField()
    PostScriptName = StringField()
    Status = StringField()
    FontStyleName = StringField()
    FontType = StringField()
    WritingScript = IntField()
    FullName = StringField()
    FullNameNative = StringField()
    FontStyleNameNative = StringField()
    PlatformName = StringField()
    Version = StringField()
    

class CompositeFont(Element):
    """
    A composite font is made up of multiple, separate fonts.
    
    For example, the default composite font, "[No composite font]", consists of 
    the following <CompositeFontEntry> elements: Kanji, Kana, Punctuation, 
    Symbols, Alphabetic, and Numbers. Each of the <CompositeFontEntry> elements 
    contains an <AppliedFont> property that defines the font it uses.
    """
    Self = StringField(required=True)
    Name = StringField()
    

class CompositeFontEntryProperties(Properties):
    AppliedFont = StringField()
    

class CompositeFontEntry(Element):
    Self = StringField(required=True)
    Name = StringField()
    FontStyle = StringField()
    RelativeSize = FloatField()
    HorizontalScale = FloatField()
    VerticalScale = FloatField()
    CustomCharacters = StringField()
    Locked = BooleanField()
    ScaleOption = BooleanField()
    BaselineShift = FloatField()
    
    Properties = EmbeddedDocumentField(CompositeFontEntryProperties)
