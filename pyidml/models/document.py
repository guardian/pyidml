import mongoengine
from pyidml.fields import *
from pyidml.models import Element, XMLSerializableMixin, ElementMixin, Properties, ElementEmbeddedDocumentField

class Language(Element):
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
