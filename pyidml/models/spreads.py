from pyidml.fields import *
from pyidml.models import Element, Properties

class Spread(Element):
    """
    The pages in an InDesign document are grouped into spreads and master 
    spreads.
    
    Spreads and master spreads contain pages, and all page items that can appear 
    in an InDesign document. In addition, spreads contain a number of 
    spread-level preferences, such as flattener settings, the spread binding 
    location, and the display state of master page items on the spread.
    """
    Self = StringField(required=True)
    FlattenerOverride = StringField()
    AllowPageShuffle = BooleanField()
    ItemTransform = SpaceSeparatedListField(FloatField())
    ShowMasterItems = BooleanField()
    PageCount = IntField()
    BindingLocation = IntField()
    PageTransitionType = StringField()
    PageTransitionDirection = StringField()
    PageTransitionDuration = StringField()
    
    Properties = EmbeddedDocumentField(Properties)
    
    @classmethod
    def from_xml(cls, e):
        if e[0] and e[0].tag == 'Spread':
            e = e[0]
        return super(Spread, cls).from_xml(e)
    

class MasterSpreadProperties(Properties):
    PageColor = StringField() # TODO: colortype
    

class MasterSpread(Element):
    """
    Master spreads differ from document page spreads in that they can be applied 
    to other pages, and are typically used for repeating layout elements, such 
    as page numbers or running headers.
    """
    Self = StringField(required=True)
    ItemTransform = SpaceSeparatedListField(FloatField())
    OverriddenPageItemProps = StringField() # TODO: list
    Name = StringField()
    NamePrefix = StringField()
    BaseName = StringField()
    ShowMasterItems = BooleanField()
    PageCount = IntField()
    
    Properties = EmbeddedDocumentField(MasterSpreadProperties)
    
    @classmethod
    def from_xml(cls, e):
        if e[0] and e[0].tag == 'MasterSpread':
            e = e[0]
        return super(MasterSpread, cls).from_xml(e)
    

class PathPointType(Element):
    """
    Each <PathPoint> element contains attributes defining three coordinate pairs 
    that define the location of the path point and the curvature of the line 
    segments connecting the path point to the other points in the path.
    
    These attributes are named PathPointAnchor (the location of the point), 
    LeftDirection (incoming Bezier control point), and RightDirection (outgoing 
    Bezier control point). Each of these attributes take the form x y (where x 
    is the horizontal location of the point and y is the vertical location, 
    expressed in the inner coordinate system of the page item).
    """
    Anchor = SpaceSeparatedListField(FloatField())
    LeftDirection = SpaceSeparatedListField(FloatField())
    RightDirection = SpaceSeparatedListField(FloatField())
    

class PathPoint(PathPointType):
    pass
    

class GeometryPathType(Element):
    """
    <GeometryPathType> elements represent the paths that make up the page item.
    """
    PathPointArray = ListField(EmbeddedDocumentField(PathPointType))
    PathOpen = BooleanField()
    

class PageItemProperties(Properties):
    PathGeometry = ListField(EmbeddedDocumentField(GeometryPathType))
    

class PageItem(Element):
    """
    Page items are the rectangles, ellipses, graphic lines, polygons, text 
    frames, groups, and buttons that can appear on an InDesign page. In IDML, 
    page items are collected on spreads as child elements of the <Spread> 
    element.
    
    Page items appear in elements named after their specific class: Rectangle, 
    Oval, GraphicLine, Polygon, TextFrame, Group, and Button. There is no 
    specific page item for a graphic frame; any rectangle, ellipse, graphic 
    line, or polygon can contain an imported graphic. The only difference 
    between the Rectangle, Oval, GraphicLine, and Polygon elements is in the 
    number and arrangement of the PathPoint elements contained in their 
    PathGeometry elements.
    
    From the point of view of the InDesign scripting model, page items 
    frequently change their type as you alter their content type or geometry. 
    Add a point to a rectangle, and it becomes a polygon; change the content 
    type of a polygon to text type, and it becomes a text frame. IDML works in a 
    similar fashion-you can add multiple paths to a <Rectangle> element, for 
    example, and InDesign will still be able to open and interpret the 
    element.
    
    There are no <PageItem> elements in IDML; this element is provided for 
    explanatory purposes only - it could be a <Rectangle>, <Oval>, 
    <GraphicLine>, <TextFrame>, or <Polygon> element.
    """
    Self = StringField(required=True)
    ContentType = StringField()
    StoryTitle = StringField()
    AllowOverrides = BooleanField()
    FillColor = StringField()
    FillTint = FloatField()
    OverprintFill = BooleanField()
    CornerRadius = FloatField()
    StrokeWeight = FloatField()
    MiterLimit = FloatField()
    EndCap = StringField()
    EndJoin = StringField()
    StrokeType = StringField()
    StrokeCornerAdjustment = StringField()
    StrokeDashAndGap = StringField() # TODO: list
    LeftLineEnd = StringField()
    RightLineEnd = StringField()
    StrokeColor = StringField()
    StrokeTint = FloatField()
    GradientFillStart = StringField() # TODO: UnitPointType_TypeDef
    GradientFillLength = FloatField()
    GradientFillAngle = FloatField()
    GradientStrokeStart = StringField() # TODO: UnitPointType_TypeDef
    GradientStrokeLength = FloatField()
    GradientStrokeAngle = FloatField()
    OverprintStroke = BooleanField()
    GapColor = StringField()
    GapTint = FloatField()
    OverprintGap = BooleanField()
    StrokeAlignment = StringField()
    Nonprinting = BooleanField()
    ItemLayer = StringField()
    Locked = BooleanField()
    LocalDisplaySetting = StringField()
    GradientFillHiliteLength = FloatField()
    GradientFillHiliteAngle = FloatField()
    GradientStrokeHiliteLength = FloatField()
    GradientStrokeHiliteAngle = FloatField()
    AppliedObjectStyle = StringField()
    CornerOption = StringField()
    Visible = BooleanField()
    Name = StringField()
    TopLeftCornerOption = StringField()
    TopRightCornerOption = StringField()
    BottomLeftCornerOption = StringField()
    BottomRightCornerOption = StringField()
    TopLeftCornerRadius = FloatField()
    TopRightCornerRadius = FloatField()
    BottomLeftCornerRadius = FloatField()
    BottomRightCornerRadius = FloatField()
    ItemTransform = SpaceSeparatedListField(FloatField())
    
    Properties = EmbeddedDocumentField(PageItemProperties)
    

class Rectangle(PageItem):
    pass
    

class Oval(PageItem):
    pass
    

class GraphicLine(PageItem):
    pass
    

class Polygon(PageItem):
    pass
    

class TextFrame(PageItem):
    pass
    

class AnimationDataPathKeyFrameType(Element):
    KeyFrame = IntField()
    PathPoint = EmbeddedDocumentField(PathPoint)


class AnimationSettingProperties(Element):
    Preset = StringField()
    MotionPathPoints = ListField(EmbeddedDocumentField(GeometryPathType))
    MotionPath = ListField(
        EmbeddedDocumentField(AnimationDataPathKeyFrameType)
    )
    OpacityArray = ListField(
        EmbeddedDocumentField(AnimationDataPathKeyFrameType)
    )
    RotationArray = ListField(
        EmbeddedDocumentField(AnimationDataPathKeyFrameType)
    )
    ScaleXArray = ListField(
        EmbeddedDocumentField(AnimationDataPathKeyFrameType)
    )
    ScaleXArray = ListField(
        EmbeddedDocumentField(AnimationDataPathKeyFrameType)
    )
    

class AnimationSetting(Element):
    """
    The animation of a page item exported to a SWF document is controlled by the 
    properties of the <AnimationSetting> element of the page item element.
    """
    TransformOffsets = SpaceSeparatedListField(FloatField())
    Duration = FloatField()
    DesignOption = StringField()
    EaseType = StringField()
    Plays = IntField()
    PlaysLoop = BooleanField()
    InitiallyHidden = BooleanField()
    HiddenAfter = BooleanField()
    HasCustomSettings = BooleanField()
    


# TODO: Animation Timing


class GraphicProperties(Properties):
    Contents = StringField()
    GraphicProxy = StringField()
    ClippingPathGeometry = ListField(EmbeddedDocumentField(GeometryPathType))
    

class BaseGraphic(Element):
    """
    Placed (imported) graphics always appear inside a spline item. This spline 
    item can be a rectangle, a graphic line, an oval, or a polygon (these spline 
    items can be nested inside a <State> element of a <Button> element or a 
    <MultiStateObject> element). There is no special class of page item for a 
    graphic frame.
    
    The imported graphic itself can be an <Image>, a <PDF>, an <ImportedPage>, 
    an <EPS>, a <PICT>, or a <WMF>. All of these elements share the attributes 
    and elements of the <Graphic> object, and add a few attributes and elements 
    specific to their specific object type. <WMF> and <PICT> elements are 
    identical to <Graphic>.
    """
    Self = StringField(required=True)
    LocalDisplaySetting = StringField()
    ImageTypeName = StringField()
    AppliedObjectStyle = StringField()
    ItemTransform = SpaceSeparatedListField(FloatField())
    FillColor = StringField()
    FillTint = FloatField()
    OverprintFill = BooleanField()
    CornerRadius = BooleanField()
    StrokeWeight = BooleanField()
    MiterLimit = FloatField()
    EndCap = StringField()
    EndJoin = StringField()
    StrokeType = StringField()
    StrokeCornerAdjustment = StringField()
    StrokeDashAndGap = SpaceSeparatedListField(FloatField())
    LeftLineEnd = StringField()
    RightLineEnd = StringField()
    StrokeColor = StringField()
    StrokeTint = FloatField()
    GradientFillStart = SpaceSeparatedListField(FloatField())
    GradientFillLength = FloatField()
    GradientFillAngle = FloatField()
    GradientStrokeStart = SpaceSeparatedListField(FloatField())
    GradientStrokeLength = FloatField()
    GradientStrokeAngle = FloatField()
    OverprintStroke = BooleanField()
    GapColor = StringField()
    GapTint = FloatField()
    OverprintGap = BooleanField()
    StrokeAlignment = StringField()
    Nonprinting = BooleanField()
    ItemLayer = StringField()
    Locked = BooleanField()
    GradientFillHiliteLength = FloatField()
    GradientFillHiliteAngle = FloatField()
    GradientStrokeHiliteLength = FloatField()
    GradientStrokeHiliteAngle = FloatField()
    CornerOption = StringField()
    Visible = BooleanField()
    Name = StringField()
    TopLeftCornerOption = StringField()
    TopRightCornerOption = StringField()
    BottomLeftCornerOption = StringField()
    BottomRightCornerOption = StringField()
    TopLeftCornerRadius = FloatField()
    TopRightCornerRadius = FloatField()
    BottomLeftCornerRadius = FloatField()
    BottomRightCornerRadius = FloatField()
    
    Properties = EmbeddedDocumentField(GraphicProperties)
    

class WMF(BaseGraphic):
    pass
    

class PICT(BaseGraphic):
    pass
    

class ImageProperties(GraphicProperties):
    Profile = StringField() # TODO: colour profiles

class Image(BaseGraphic):
    ActualPpi = SpaceSeparatedListField(FloatField())
    EffectivePpi = SpaceSeparatedListField(FloatField())
    ImageRenderingIntent = StringField()
    Space = StringField()
    
    Properties = EmbeddedDocumentField(ImageProperties)
    

class PDFAttribute(Element):
    PageNumber = IntField()
    PDFCrop = StringField()
    TransparentBackground = BooleanField()
    

class PDF(BaseGraphic):
    ActualPPI = SpaceSeparatedListField(FloatField())
    CMYKVectorPolicy = StringField()
    EffectivePpi = SpaceSeparatedListField(FloatField())
    GrayVectorPolicy = StringField()
    RGBVectorPolicy = StringField()
    Space = StringField()
    

class EPS(PDF):
    pass
    

class ImportedPage(BaseGraphic):
    """
    InDesign can import pages from other InDesign documents as graphics.
    """
    ImportedPageCrop = StringField()
    PageNumber = IntField()
    

class NavigationPoint(Element):
    """
    A <NavigationPoint> element in a <Movie> element represents a cue point in 
    the video.
    """
    Self = StringField(required=True)
    Id = IntField()
    Name = StringField()
    Time = FloatField()
    

class Movie(PageItem):
    """
    InDesign can place movie and sound files into a document. These media files 
    can be played in exported SWF and PDF files.
    """
    CanChoosePosters = BooleanField()
    ControllerSkin = StringField()
    CustomPoster = BooleanField()
    Description = StringField()
    EmbedInPDF = BooleanField()
    FilePath = StringField()
    FloatingWindow = BooleanField()
    FloatingWindowPosition = StringField()
    FloatingWindowSize = StringField()
    IntrinsicBounds = SpaceSeparatedListField(IntField())
    MovieLoop = BooleanField()
    PlayMode = StringField()
    PlayOnPageTurn = BooleanField()
    PosterAvailable = BooleanField()
    ShowController = BooleanField()
    ShowControls = BooleanField()
    URL = StringField()
    
    
class Sound(PageItem):
    Description = StringField()
    DoNotPrintPoster = BooleanField()
    EmbedInPDF = BooleanField()
    FilePath = StringField()
    SoundLoop = BooleanField()
    StopOnPageTurn = BooleanField()
    

class TextFrame(PageItem):
    ParentStory = StringField()
    PreviousTextFrame = StringField()
    NextTextFrame = StringField()
    

class TextFramePreferenceProperties(Element):
    InsetSpacing = StringField() # TODO: ListItems
    

class TextFramePreference(Element):
    """
    The <TextFramePreference> element contains attributes and elements that 
    control properties such as number of columns in the text frame, the text 
    frame inset distances, and the method used to calculate the location of the 
    first baseline of text in the text frame.
    """
    TextColumnCount = IntField()
    TextColumnGutter = FloatField()
    TextColumnFixedWidth = FloatField()
    UseFixedColumnWidth = BooleanField()
    FirstBaselineOffset = StringField()
    MinimumFirstBaselineOffset = FloatField()
    VerticalJustification = StringField()
    VerticalThreshold = FloatField()
    IgnoreWrap = BooleanField()
    VerticalBalanceColumns = BooleanField()
    

class BaselineFrameGridOptionsProperties(Element):
    BaselineFrameGridColor = StringField() # TODO: InDesignUIColorType_TypeDef
    

class BaselineFrameGridOptions(Element):
    """
    Text frames can also contain a <BaselineFrameGridOption> element. This 
    element contains properties expressed as attributes and elements that 
    control the baseline grid options for the text frame.
    
    The baseline frame grid affects paragraphs in the text frame that have been 
    set to snap to the baseline grid-if the UseCustomBaselineGrid attribute is 
    true, then the baselines of the paragraphs will snap to the grid defined by 
    the <BaselineFrameGrid> element; it it's false, they'll snap to the document 
    baseline grid (which is defined in the <GridPreference> element)
    """
    UseCustomBaselineFrameGrid = BooleanField()
    StartingOffsetForBaselineFrameGrid = FloatField()
    BaselineFrameGridRelativeOption = StringField()
    BaselineFrameGridIncrement = FloatField()
    
    Properties = EmbeddedDocumentField(BaselineFrameGridOptionsProperties)
    

class TransparencySetting(Element):
    """
    You can apply transparency effects to page items in an InDesign layout. In 
    IDML, you accomplish this using the <TransparencySetting> element. A child 
    element (or elements) of this element specify the transparency effect you 
    want to apply.
    """
    pass
    

class BlendingSetting(Element):
    BlendMode = StringField()
    Opacity = FloatField()
    KnockoutGroup = BooleanField()
    IsolateBlending = BooleanField()
    

class DropShadowSetting(Element):
    Distance = FloatField()
    Angle = FloatField()
    Mode = StringField()
    BlendMode = StringField()
    Opacity = FloatField()
    XOffset = FloatField()
    YOffset = FloatField()
    Size = FloatField()
    EffectColor = StringField()
    Noise = FloatField()
    Spread = FloatField()
    UseGlobalLight = BooleanField()
    KnockedOut = BooleanField()
    HonorOtherEffects = BooleanField()
    

class FeatherSetting(Element):
    Mode = StringField()
    Width = FloatField()
    CornerType = StringField()
    Noise = FloatField()
    ChokeAmount = FloatField()
    

class InnerShadowSetting(Element):
    XOffset = FloatField()
    YOffset = FloatField()
    Applied = BooleanField()
    EffectColor = StringField()
    BlendMode = StringField()
    Opacity = FloatField()
    Angle = FloatField()
    Distance = FloatField()
    UseGlobalLight = BooleanField()
    ChokeAmount = FloatField()
    Size = FloatField()
    Noise = FloatField()
    

class OuterGlowSetting(Element):
    Applied = BooleanField()
    BlendMode = StringField()
    Opacity = FloatField()
    Noise = FloatField()
    EffectColor = StringField()
    Technique = StringField()
    Spread = FloatField()
    Size = FloatField()
    

class InnerGlowSetting(Element):
    Applied = BooleanField()
    BlendMode = StringField()
    Opacity = FloatField()
    Noise = FloatField()
    EffectColor = StringField()
    Technique = StringField()
    Spread = FloatField()
    Size = FloatField()
    Source = StringField()
    

class BevelAndEmbossSetting(Element):
    Applied = BooleanField()
    Style = StringField()
    Technique = StringField()
    Depth = FloatField()
    Direction = StringField()
    Size = FloatField()
    Soften = FloatField()
    Angle = FloatField()
    Altitude = FloatField()
    UseGlobalLight = BooleanField()
    HighlightColor = StringField()
    HighlightBlendMode = StringField()
    HighlightOpacity = FloatField()
    ShadowColor = StringField()
    ShadowBlendMode = StringField()
    ShadowOpacity = FloatField()
    

class SatinSetting(Element):
    Applied = BooleanField()
    EffectColor = StringField()
    BlendMode = StringField()
    Opacity = FloatField()
    Angle = FloatField()
    Distance = FloatField()
    Size = FloatField()
    InvertEffect = BooleanField()
    

class DirectionalFeatherSetting(Element):
    Applied = BooleanField()
    LeftWidth = FloatField()
    RightWidth = FloatField()
    TopWidth = FloatField()
    BottomWidth = FloatField()
    ChokeAmount = FloatField()
    Angle = FloatField()
    FollowShapeMode = StringField()
    Noise = FloatField()
    

class GradientFeatherSetting(Element):
    Applied = BooleanField()
    Type = StringField()
    Angle = FloatField()
    Length = FloatField()
    GradientStart = SpaceSeparatedListField(FloatField())
    HiliteAngle = FloatField()
    HiliteLength = FloatField()
    

class OpacityGradientStop(Element):
    Self = StringField(required=True)
    Opacity = FloatField()
    Location = FloatField()
    Midpoint = FloatField()
    

class Group(PageItem):
    """
    InDesign page items can be grouped, and groups can contain other groups. 
    Each object stored inside a group is represented as a child element of the 
    <Group> element, as shown in the following example.
    """
    

# TODO: Button, Behavior, MultiStateObject, XMLElement


class PageProperties(Properties):
    Descriptor = StringField() # TODO
    PageColor = StringField() # TODO: InDesignUIColorType_TypeDef
    

class Page(Element):
    """
    Spreads contain one or more pages.
    
    The pages in a spread are stored as <Page> elements, which properties that 
    override document- or spread-based settings, such as trapping presets, the 
    applied master spread, and page margin settings. Pages in a spread can be of 
    multiple sizes, and are added to the spread based on the order in which they 
    appear inside the <Spread> element.
    
    The location of the pages inside the spread is determined by the binding 
    direction of the document, which is defined by the BindingLocation attribute 
    of the <Spread> element-refer to the InDesign documentation for more 
    information on binding direction.
    """
    Self = StringField(required=True)
    GeometricBounds = SpaceSeparatedListField(FloatField())
    ItemTransform = SpaceSeparatedListField(FloatField())
    Name = StringField()
    AppliedTrapPreset = StringField()
    OverrideList = SpaceSeparatedListField(StringField())
    AppliedMaster = StringField()
    MasterPageTransform = SpaceSeparatedListField(FloatField())
    TabOrder = SpaceSeparatedListField(StringField())
    GridStartingPoint = StringField()
    UseMasterGrid = BooleanField()
    
    Properties = EmbeddedDocumentField(PageProperties)
    

class MarginPreference(Element):
    """
    The columns and margins of a page are defined by the <MarginPreference> 
    object.
    """
    ColumnCount = IntField()
    ColumnGutter = FloatField()
    Top = FloatField()
    Bottom = FloatField()
    Left = FloatField()
    Right = FloatField()
    ColumnDirection = StringField()
    ColumnsPositions = SpaceSeparatedListField(FloatField())
    

class GuidesProperties(Properties):
    GuideColor = StringField() # TODO: InDesignUIColorType_TypeDef
    

class Guides(Element):
    """
    In addition to page items, InDesign spreads can contain guides. 
    """
    Self = StringField(required=True)
    Orientation = StringField()
    Location = FloatField()
    FitToPage = BooleanField()
    ViewThreshold = FloatField()
    Locked = BooleanField()
    ItemLayer = StringField()
    PageIndex = IntField()
    
    Properties = EmbeddedDocumentField(GuidesProperties)
    

class FlattenerPreferenceProperties(Element):
    RasterVectorBalance = StringField()
    

class FlattenerPreference(Element):
    """
    The appearance of transparency (including the Drop Shadow, Inner Shadow, 
    Outer Glow, Inner Glow, Bevel and Emboss, Satin, and Feather effects) when 
    you print or export an InDesign document depends on the flattener settings 
    for the spread and/or the document (the exact appearance of the transparent 
    objects on the printed pages or in the exported file depends on the 
    capabilities of the printer or file format).
    
    The flattener settings of the document apply to all objects unless the 
    objects exist on a spread which has been assigned its own flattener 
    settings; in that case, the flattener settings of the spread override those 
    of the document. In IDML, these settings are represented by the 
    <FlattenerPreference> element.
    """
    LineArtAndTextResolution = FloatField()
    GradientAndMeshResolution = FloatField()
    ClipComplexRegions = BooleanField()
    ConvertAllStrokesToOutlines = BooleanField()
    ConvertAllTextToOutlines = BooleanField()
    
    Properties = EmbeddedDocumentField(FlattenerPreferenceProperties)
    



