import mongoengine
from pyidml.fields import *
from pyidml.models import Element, XMLSerializableMixin, ElementMixin, Properties, ElementEmbeddedDocumentField
from pyidml.models.backing_story import BackingStory
from pyidml.models.fonts import Fonts
from pyidml.models.graphic import Graphic
from pyidml.models.preferences import Preferences
from pyidml.models.styles import Styles
from pyidml.models.tags import Tags

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
    Id = IntField() # new in 7.0
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
    
    Fonts = EmbeddedDocumentField(Fonts)
    Graphic = EmbeddedDocumentField(Graphic)
    Preferences = EmbeddedDocumentField(Preferences)
    Properties = EmbeddedDocumentField(Properties)
    Styles = EmbeddedDocumentField(Styles)
    Tags = EmbeddedDocumentField(Tags)
    
    children = ListField(ElementEmbeddedDocumentField())
    
    def get_story(self, name):
        for story in self.get_children('Story'):
            if story.Self == name:
                return story
    

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
    

class ConditionProperties(Properties):
    IndicatorColor = StringField()
    

class Condition(Element):
    """
    InDesign documents can feature conditional text-text that is only visible in 
    the layout when a specific state is enabled. The <Condition> element 
    controls the appearance of the text governed by a condition.
    """
    Self = StringField(required=True)
    Name = StringField(required=True)
    IndicatorMethod = StringField()
    UnderlineIndicatorAppearance = StringField()
    Visible = BooleanField()
    
    Properties = EmbeddedDocumentField(ConditionProperties)
    

class VisibilityPair(Element):
    Condition = StringField(required=True)
    Visibility = BooleanField(required=True)
    

class ConditionSetProperties(Properties):
    SetConditions = ListField(EmbeddedDocumentField(VisibilityPair))
    

class ConditionSet(Element):
    Self = StringField(required=True)
    Name = StringField(required=True)
    
    Properties = EmbeddedDocumentField(ConditionSetProperties)


class ConditionalTextPreference(Element):
    Self = StringField(required=True)
    ShowConditionIndicators = StringField()
    ActiveConditionSet = StringField()
    

class TextVariable(Element):
    """
    A text variable is an item you insert in text that varies according to the 
    context.
    
    For example, the Last Page Number variable displays the page number of the 
    last page of the document. If you add or remove pages, the variable is 
    updated accordingly.
    """
    Self = StringField(required=True)
    Name = StringField(required=True)
    VariableType = StringField()

class BaseTextVariable(Element):
    Self = StringField(required=True)
    TextBefore = StringField()
    TextAfter = StringField()


class CustomTextVariablePreferenceProperties(Element):
    Contents = StringField()


class CustomTextVariablePreference(Element):
    Self = StringField(required=True)
    
    Properties = EmbeddedDocumentField(CustomTextVariablePreferenceProperties)


class FileNameVariablePreference(BaseTextVariable):
    IncludePath = BooleanField()
    IncludeExtension = BooleanField()
    

class PageNumberVariablePreference(BaseTextVariable):
    Format = StringField()
    Scope = StringField()
    

class ChapterNumberVariablePreference(BaseTextVariable):
    Format = StringField()
    

class DateVariablePreference(BaseTextVariable):
    Format = StringField()


class MatchCharacterStylePreference(BaseTextVariable):
    AppliedCharacterStyle = StringField()
    ChangeCase = StringField()
    DeleteEndPunctuation = BooleanField()
    SearchStrategy = StringField()
    

class MatchParagraphStylePreference(BaseTextVariable):
    AppliedCharacterStyle = StringField()
    ChangeCase = StringField()
    DeleteEndPunctuation = BooleanField()
    SearchStrategy = StringField()
    

class CaptionMetadataVariablePreference(BaseTextVariable):
    MetadataProviderName = StringField()
    

class LayerProperties(Properties):
    LayerColor = StringField()
    

class Layer(Element):
    """
    InDesign documents can contain layers, which are transparent planes on which 
    you can arrange the page items in your layout.
    
    Layers can be used to control the stacking order of objects in a document, 
    but they can also be used to organize objects in a document. Layers in an 
    InDesign document are document-wide. In IDML, <Layer> elements appear inside 
    the <Document> element in the designmap.xml file.
    """
    Self = StringField(required=True)
    Name = StringField()
    Visible = BooleanField()
    Locked = BooleanField()
    IgnoreWrap = BooleanField()
    ShowGuides = BooleanField()
    LockGuides = BooleanField()
    UI = BooleanField()
    Expendable = BooleanField()
    Printable = BooleanField()
    
    Properties = EmbeddedDocumentField(LayerProperties)
    

class Section(Element):
    """
    Page ranges in an InDesign document can be broken up into sections.
    
    Section properties control the page numbering system in use in the pages of 
    the section.
    """
    Self = StringField(required=True)
    Length = IntField()
    Name = StringField()
    PageNumberStyle = StringField()
    ContinueNumbering = BooleanField()
    IncludeSectionPrefix = BooleanField()
    PageNumberStart = IntField()
    Marker = StringField()
    PageStart = StringField()
    SectionPrefix = StringField()
    
    Properties = EmbeddedDocumentField(Properties)
    

class CrossReferenceFormat(Element):
    """
    InDesign documents can contain cross references. Cross references are made 
    up of <BuildingBlock> elements.
    """
    Self = StringField(required=True)
    Name = StringField(required=True)
    AppliedCharacterStyle = StringField()
    
    Properties = EmbeddedDocumentField(Properties)
    

class BuildingBlock(Element):
    """
    Cross references are made up of "building blocks" - elements that specify 
    text and text formatting that can be added to a cross reference (for more on 
    building blocks, refer to the InDesign documentation).
    
    The <CrossReferenceFormat> element can contain multiple <BuildingBlock> 
    elements.
    """
    Self = StringField(required=True)
    BlockType = StringField(required=True)
    AppliedCharacterStyle = StringField()
    CustomText = StringField()
    AppliedDelimiter = StringField()
    IncludeDelimiter = BooleanField()
    

class HyperlinkProperties(Properties):
    BorderColor = StringField()
    Destination = StringField()


class Hyperlink(Element):
    """
    You can create hyperlinks in an InDesign document so that when you export to 
    PDF, a viewer can click a link to jump to other locations in the same PDF 
    document, to other PDF documents, or to web sites. Hyperlinks are made up of 
    a hyperlink source and a hyperlink destination, and various 
    display/formatting options.
    
    A hyperlink source is hyperlinked text, a hyperlinked text frame, or a 
    hyperlinked graphics frame. A hyperlink destination is the URL, position in 
    text, or page to which a hyperlink jumps. A source can jump to only one 
    destination, but any number of sources can jump to the same destination.
    """
    Self = StringField(required=True)
    Name = StringField()
    Source = StringField(required=True)
    Visible = BooleanField()
    Highlight = StringField()
    Width = StringField()
    BorderStyle = StringField()
    Hidden = BooleanField()
    DestinationUniqueKey = IntField()
    
    Properties = EmbeddedDocumentField(HyperlinkProperties)
    

class HyperlinkPageDestinationProperties(Properties):
    ViewBounds = StringField(required=True)
    

class HyperlinkPageDestination(Element):
    """
    A hyperlink page destination specifies a page in the document as the 
    destination for a hyperlink.
    """
    Self = StringField(required=True)
    Name = StringField()
    NameManually = BooleanField()
    DestinationPage = StringField()
    ViewSetting = StringField()
    ViewPercentage = FloatField()
    Hidden = BooleanField()
    DestinationUniqueKey = IntField()
    
    Properties = EmbeddedDocumentField(HyperlinkPageDestinationProperties)
    

class HyperlinkURLDestination(Element):
    """
    A hyperlink page destination specifies a web address as the destination for 
    a hyperlink.
    """
    Self = StringField(required=True)
    Name = StringField()
    DestinationURL = StringField()
    Hidden = BooleanField()
    DestinationUniqueKey = IntField()
    
    Properties = EmbeddedDocumentField(Properties)
    

class HyperlinkExternalPageDestination(Element):
    """
    A hyperlink page destination specifies a page outside the document as the 
    destination for a hyperlink.
    """
    Self = StringField(required=True)
    Name = StringField()
    DocumentPath = StringField()
    DestinationPageIndex = IntField()
    ViewSetting = StringField()
    ViewPercentage = FloatField()
    Hidden = BooleanField()
    DestinationUniqueKey = IntField()
    
    Properties = EmbeddedDocumentField(HyperlinkPageDestinationProperties)
    

class HyperlinkPageItemSource(Element):
    """
    A hyperlink page item source is a hyperlink associated with a page item.
    """
    Self = StringField(required=True)
    Name = StringField()
    SourcePageItem = StringField(required=True)
    Hidden = BooleanField()
    
    Properties = EmbeddedDocumentField(Properties)
    

class Bookmark(Element):
    """
    InDesign documents can add bookmarks for navigation in PDFs you export.
    """
    Self = StringField(required=True)
    Name = StringField()
    Destination = StringField(required=True)
    
    Properties = EmbeddedDocumentField(Properties)
    

class KinsokuTable(Element):
    Self = StringField(required=True)
    Name = StringField(required=True)
    CantBeginLineChars = StringField()
    CantEndLineChars = StringField()
    HangingPunctuationChars = StringField()
    CantBeSeparatedChars = StringField()
    
    Properties = EmbeddedDocumentField(Properties)
    

class OverrideMojikumiAkiType(Element):
    TargetMojikumiClass = IntField(required=True)
    SideMojikumiClass = IntField(required=True)
    SideIsAfterTarget = BooleanField(required=True)
    Minimum = FloatField(required=True)
    Desired = FloatField(required=True)
    Maximum = FloatField(required=True)
    CompressionPriority = IntField(required=True)
    AkiDoesNotFloat = BooleanField(required=True)
    

class MojikumiTableProperties(Properties):
    OverrideMojikumiAkiList = ListField(
        EmbeddedDocumentField(OverrideMojikumiAkiType)
    )

class MojikumiTable(Element):
    Self = StringField(required=True)
    Name = StringField(required=True)
    BasedOnMojikumiSet = StringField()
    
    Properties = EmbeddedDocumentField(MojikumiTableProperties)
    

class NumberingList(Element):
    Self = StringField(required=True)
    Name = StringField(required=True)
    ContinueNumbersAcrossStories = BooleanField()
    ContinueNumbersAcrossDocuments = BooleanField()
    
    Properties = EmbeddedDocumentField(Properties)
    

class NamedGrid(Element):
    Self = StringField(required=True)
    Name = StringField(required=True)
    
    Properties = EmbeddedDocumentField(Properties)
    

class GridDataInformationProperties(Properties):
    AppliedFont = StringField()
    

class GridDataInformation(Element):
    FontStyle = StringField()
    PointSize = FloatField()
    CharacterAki = FloatField()
    LineAki = FloatField()
    HorizontalScale = FloatField()
    VerticalScale = FloatField()
    LineAlignment = StringField()
    GridAlignment = StringField()
    CharacterAlignment = StringField()
    GridView = StringField()
    CharacterCountLocation = StringField()
    CharacterCountSize = FloatField()
    
    Properties = EmbeddedDocumentField(GridDataInformationProperties)
    

class MetadataPacketPreferenceProperties(Element):
    Contents = StringField()

class MetadataPacketPreference(Element):
    Properties = EmbeddedDocumentField(MetadataPacketPreferenceProperties)
    

class DocumentUserProperties(Element):
    UserColor = StringField()
    

class DocumentUser(Element):
    Self = StringField(required=True)
    UserName = StringField(required=True)
    
    Properties = EmbeddedDocumentField(DocumentUserProperties)
    

class Index(Element):
    Self = StringField(required=True)
    
    Properties = EmbeddedDocumentField(Properties)
    

class Topic(Element):
    Self = StringField(required=True)
    SortOrder = StringField()
    Name = StringField(required=True)
    
class CrossReference(Element):
    Self = StringField(required=True)
    ReferencedTopic = StringField()
    CrossReferenceType = StringField()
    CustomTypeString = StringField()
    
    Properties = EmbeddedDocumentField(Properties)
    

class PreflightProfile(Element):
    Self = StringField(required=True)
    Name = StringField()
    Description = StringField()
    
    Properties = EmbeddedDocumentField(Properties)
    

class PreflightProfileRule(Element):
    Self = StringField(required=True)
    Name = StringField()
    Id = StringField(required=True)
    Description = StringField()
    Flag = StringField()
    
    Properties = EmbeddedDocumentField(Properties)
    

class RuleDataObject(Element):
    """
    TODO: Not implemented
    """
    

class PreflightRuleInstance(PreflightProfileRule):
    pass


class DataMergeImagePlaceholder(Element):
    Self = StringField(required=True)
    Field = StringField(required=True)
    PlaceholderPageItem = StringField(required=True)
    

class HyphenationException(Element):
    Self = StringField(required=True)
    Name = StringField(required=True)
    RemovedExceptions = StringField() # FIXME: list?
    AddedExceptions = StringField() # FIXME: list?
    

class IndexingSortOption(Element):
    """
    The <IndexingSortOptions> elements defines the default indexing sort options 
    for the document.
    """
    Self = StringField(required=True)
    Name = StringField(required=True)
    Include = BooleanField()
    Priority = IntField()
    HeaderType = StringField()
    

class ABulletProperties(Element):
    BulletsFont = StringField()
    BulletsFontStyle = StringField()
    

class ABullet(Element):
    Self = StringField(required=True)
    CharacterType = StringField()
    CharacterValue = IntField()
    
    Properties = EmbeddedDocumentField(ABulletProperties)
    

class AssignmentProperties(Properties):
    FrameColor = StringField()
    

class Assignment(Element):
    """
    The <Assignment> element defines the default assignment used in the 
    document.
    """
    Self = StringField(required=True)
    Name = StringField()
    UserName = StringField()
    ExportOptions = StringField()
    IncludeLinksWhenPackage = BooleanField()
    FilePath = StringField(required=True)
    
    Properties = EmbeddedDocumentField(AssignmentProperties)
    

class AssignedStory(Element):
    Self = StringField(required=True)
    Name = StringField()
    StoryReference = StringField()
    FilePath = StringField()
    
    Properties = EmbeddedDocumentField(Properties)
    

class MotionPresetProperties(Properties):
    Contents = StringField()
    

class MotionPreset(Element):
    """
    InDesign includes a number of motion presets-default animation settings that 
    can be applied to page items in an InDesign document. (new in 7.0)
    """
    Self = StringField(required=True)
    Name = StringField()
    EditLocked = BooleanField()
    DeleteLocked = BooleanField()
    NameLocked = BooleanField()
    
    Properties = EmbeddedDocumentField(MotionPresetProperties)
    

class WatermarkPreferenceProperties(Element):
    WatermarkFontColor = StringField()


class WatermarkPreference(Element):
    """
    (new in 7.0)
    """
    WatermarkVisibility = BooleanField()
    WatermarkDoPrint = BooleanField()
    WatermarkDrawInBack = BooleanField()
    WatermarkText = StringField()
    WatermarkFontFamily = StringField()
    WatermarkFontStyle = StringField()
    WatermarkFontPointSize = IntField()
    WatermarkOpacity = IntField()
    WatermarkRotation = IntField()
    WatermarkHorizontalPosition = StringField()
    WatermarkHorizontalOffset = FloatField()
    WatermarkVerticalPosition = StringField()
    WatermarkVerticalOffset = FloatField()
    

