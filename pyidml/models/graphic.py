from pyidml.fields import *
from pyidml.models import Element, Properties

class Swatch(Element):
    Self = StringField(required=True)
    Name = StringField(required=True)
    ColorEditable = BooleanField()
    ColorRemovable = BooleanField()
    Visible = BooleanField()
    SwatchCreatorID = IntField()
    

class Color(Swatch):
    Model = StringField()
    Space = StringField()
    ColorValue = SpaceSeparatedListField(FloatField())
    ColorOverride = StringField()
    BaseColor = StringField()
    SpotInkAliasSpotColorReference = StringField()
    AlternateSpace = StringField()
    AlternateColorValue = SpaceSeparatedListField(FloatField())
    

class Gradient(Swatch):
    Type = StringField()

class GradientStop(Element):
    Self = StringField(required=True)
    StopColor = StringField()
    Location = FloatField()
    Midpoint = FloatField()
    

class Tint(Swatch):
    AlternateColorValue = SpaceSeparatedListField(FloatField())
    AlternateSpace = StringField()
    BaseColor = StringField(required=True)
    ColorOverride = StringField()
    SpotInkAliasSpotColorReference = StringField()
    TintValue = FloatField()


class MixedInk(Swatch):
    BaseColor = StringField(required=True)
    InkList = SpaceSeparatedListField(StringField())
    InkNameList = SpaceSeparatedListField(StringField())
    InkPercentages = SpaceSeparatedListField(FloatField())
    MixedInkSpotColorList = SpaceSeparatedListField(StringField())
    MixedInkSpotColorNameList = SpaceSeparatedListField(StringField())
    Model = StringField()
    Space = StringField()


class MixedInkGroup(Swatch):
    InkList = SpaceSeparatedListField(StringField(), required=True)
    InkNameList = SpaceSeparatedListField(StringField())
    MixedInkSpotColorList = SpaceSeparatedListField(StringField())
    MixedInkSpotColorNameList = SpaceSeparatedListField(StringField())
    Model = StringField()


class Ink(Element):
    Self = StringField(required=True)
    Name = StringField(required=True)
    AliasInkName = StringField()
    Angle = FloatField()
    ConvertToProcess = BooleanField()
    Frequency = FloatField()
    InkType = StringField()
    NeutralDensity = FloatField()
    PrintInk = BooleanField()
    TrapOrder = IntField()


class StrokeStyle(Element):
    Self = StringField(required=True)
    Name = StringField(required=True)


class DashedStrokeStyle(Element):
    Self = StringField(required=True)
    Name = StringField(required=True)
    DashArray = SpaceSeparatedListField(FloatField())
    EndCap = StringField()
    StrokeCornerAdjustment = StringField()
    

class DottedStrokeStyle(Element):
    Self = StringField(required=True)
    Name = StringField(required=True)
    DotArray = SpaceSeparatedListField(FloatField())
    StrokeCornerAdjustment = StringField()


class StripedStrokeStyle(Element):
    Self = StringField(required=True)
    Name = StringField(required=True)
    StripeArray = SpaceSeparatedListField(FloatField())

class PastedSmoothShadeProperties(Properties):
    Contents = StringField()

class PastedSmoothShade(Swatch):
    ContentsVersion = IntField()
    ContentsType = StringField()
    SpotColorList = SpaceSeparatedListField(StringField())
    ContentsEncoding = StringField()
    ContentsMatrix = SpaceSeparatedListField(FloatField())
    
    Properties = EmbeddedDocumentField(PastedSmoothShadeProperties)

class Graphic(Element):
    DOMVersion = StringField(required=True)

