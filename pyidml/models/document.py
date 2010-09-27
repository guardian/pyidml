import mongoengine
from pyidml.fields import *
from pyidml.models import Element, XMLSerializableMixin, ElementMixin, Properties, ElementEmbeddedDocumentField

class Language(Element):
    """
    The <Language> elements in an IDML package define the language dictionaries 
    available for the document.
    
    You cannot create languages by adding new <Language> elements; they are 
    included for use as references (from, for example, <ParagraphStyle> elements 
    in the Styles.xml file in the Resources folder of the IDML package), and to 
    maintain round-trip fidelity for InDesign and InCopy documents.
    """
    Self = StringField(required=True)
    Name = StringField(required=True)
    SingleQuotes = StringField()
    DoubleQuotes = StringField()
    PrimaryLanguageName = StringField()
    SublanguageName = StringField()
    Id = IntField()
    HyphenationVendor = StringField()
    SpellingVendor = StringField()
    

class Document(mongoengine.Document, XMLSerializableMixin, ElementMixin):
    """
    An InDesign document.
    """
    DOMVersion = StringField(required=True)
    Self = StringField(required=True)
    
    ActiveProcess = StringField()
    TransparencyAttributeDefaultProperty = StringField()
    StoryList = SpaceSeparatedListField(StringField())
    FullName = StringField()
    Name = StringField()
    Visible = BooleanField()
    FilePath = StringField()
    Modified = BooleanField()
    Saved = BooleanField()
    ZeroPoint = SpaceSeparatedListField(FloatField())
    ActiveLayer = StringField()
    UnusedSwatches = SpaceSeparatedListField(StringField())
    Converted = BooleanField()
    Recovered = BooleanField()
    ReadOnly = BooleanField()
    CMYKProfileList = SpaceSeparatedListField(StringField())
    RGBProfileList = SpaceSeparatedListField(StringField())
    CMYKProfile = StringField()
    RGBProfile = StringField()
    SolidColorIntent = StringField()
    AfterBlendingIntent = StringField()
    DefaultImageIntent = StringField()
    RGBPolicy = StringField()
    CMYKPolicy = StringField()
    AccurateLABSpots = BooleanField()
    
    Properties = EmbeddedDocumentField(Properties)
    
    children = ListField(ElementEmbeddedDocumentField())
