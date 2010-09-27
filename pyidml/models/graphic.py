from pyidml.fields import *
from pyidml.models import Element, Properties

# TODO: Check properties exist

class Graphic(Element):
    """
    In an IDML package, the Graphic.xml file stores elements that define graphic 
    attributes in an InDesign document. Page items and text elements refer to 
    these attributes to apply formatting to page items and text.
    """
    DOMVersion = StringField(required=True)
    

class Swatch(Element):
    """
    In the InDesign user interface, all named colors, tints, gradients, and 
    mixed inks are swatches, but there is only one object whose type is 
    swatch - "None", or no color. Every InDesign document contains this special 
    swatch.
    """
    Self = StringField(required=True)
    Name = StringField(required=True)
    ColorEditable = BooleanField()
    ColorRemovable = BooleanField()
    Visible = BooleanField()
    SwatchCreatorID = IntField()
    

class Color(Swatch):
    """
    The <Color> element corresponds to a color in a document, including both 
    named and unnamed colors.
    
    The Model attribute specifies the color model, the Space attribute specifies 
    the color space, and the ColorValue attribute contains the corresponding 
    array of values that define the color in the appropriate color model. For 
    information on color models and color spaces, refer to the InDesign online 
    help.
    """
    Model = StringField()
    Space = StringField()
    ColorValue = SpaceSeparatedListField(FloatField())
    ColorOverride = StringField()
    BaseColor = StringField()
    SpotInkAliasSpotColorReference = StringField()
    AlternateSpace = StringField()
    AlternateColorValue = SpaceSeparatedListField(FloatField())
    

class Gradient(Swatch):
    """
    A gradient is a blend between two or more colors or between two tints of the 
    same color.
    
    Gradients can include the "Paper" color, process colors, spot colors, or 
    mixed inks using any color model or color space. Gradients are defined by a 
    series of gradient stops. Gradients can be linear or radial.
    
    In IDML, each <Gradient> element has a Type attribute that defines the type 
    of gradient (Linear or Radial). <Gradient> elements also contain two or more 
    <GradientStop> elements.
    """
    Type = StringField()
    

class GradientStop(Element):
    """
    A gradient stop is the point at which a gradient changes from one color to 
    another.
    
    Each <GradientStop> element contains a reference to a color in the 
    <StopColor> element, a Location attribute that specifies the location of the 
    gradient stop in the gradient (as a percentage of the total width of the 
    gradient), and a Midpoint attribute that defines the midpoint of the change 
    in color from this gradient stop to the next (as a percentage of the 
    distance between the two gradient stops).
    """
    Self = StringField(required=True)
    StopColor = StringField()
    Location = FloatField()
    Midpoint = FloatField()
    

class Tint(Swatch):
    """
    A tint is a color that is based on a percentage of another a color.
    
    The appearance of a tint is determined by attribute BaseColor (a reference 
    to the color that the tint is based on) and the attribute TintValue (the 
    percentage of the base color).
    """
    AlternateColorValue = SpaceSeparatedListField(FloatField())
    AlternateSpace = StringField()
    BaseColor = StringField(required=True)
    ColorOverride = StringField()
    SpotInkAliasSpotColorReference = StringField()
    TintValue = FloatField()
    

class MixedInk(Swatch):
    """
    A mixed ink is a swatch created by mixing inks - you can combine up to 
    sixteen spot inks, or mix one spot ink with one or more process inks.
    """
    BaseColor = StringField(required=True)
    InkList = SpaceSeparatedListField(StringField())
    InkNameList = SpaceSeparatedListField(StringField())
    InkPercentages = SpaceSeparatedListField(FloatField())
    MixedInkSpotColorList = SpaceSeparatedListField(StringField())
    MixedInkSpotColorNameList = SpaceSeparatedListField(StringField())
    Model = StringField()
    Space = StringField()
    

class MixedInkGroup(Swatch):
    """
    A mixed ink group contains a series of swatches created from incremental 
    percentages of different process and spot color inks.
    
    For example, mixing a spot ink with five tints of a the default color Black 
    (10%, 20%, 30%, 40%, and 50%) results in a mixed ink group that contains 
    five different mixed ink swatches.
    
    The mixed inks that make up a mixed ink group are the same as standalone 
    mixed inks, except that the value of the BaseColor attribute for a mixed ink 
    in a mixed ink group will contain a reference to the unique ID of the mixed 
    ink group (rather than n for "none").
    """
    InkList = SpaceSeparatedListField(StringField(), required=True)
    InkNameList = SpaceSeparatedListField(StringField())
    MixedInkSpotColorList = SpaceSeparatedListField(StringField())
    MixedInkSpotColorNameList = SpaceSeparatedListField(StringField())
    Model = StringField()
    

class Ink(Element):
    """
    Inks are used to produce specific colors in printing.
    
    For process colors, Cyan, Magenta, Yellow and Black inks are mixed together 
    to produce a range of colors. Every spot color, by contrast, represents an 
    individual ink or printing plate.
    """
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
    """
    The stroke styles used in an InDesign document are represented in an IDML 
    package by the <StrokeStyle>, <DashedStrokeStyle>, <DottedStrokeStyle>, and 
    <StripedStrokeStyle> elements in the Graphics.xml file.
    """
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
    
