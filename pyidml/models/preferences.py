from pyidml.fields import *
from pyidml.models import Element, Properties
from spreads import GeometryPathType


class DataMerge(Element):
    """
    The <DataMerge> element stores the settings that are be used by the 
    DataMerge feature of In- Design. This preference object does not have any 
    effect on the interpretation of layout elements (page items or stories, for 
    example) in the IDML file.
    """
    DataSourceFileType = StringField()
    DataSourceFile = StringField()
    

class DataMergeOption(Element):
    """
    The <DataMergeOption> element stores the preferences for the DataMerge 
    feature of InDesign.
    """
    FittingOption = StringField()
    CenterImage = BooleanField()
    LinkImages = BooleanField()
    RemoveBlankLines = BooleanField()
    CreateNewDocument = BooleanField()
    DocumentSize = IntField()
    

# TODO: LayoutAdjustmentPreference, XMLImportPeference, XMLExportPreference, XMLPreference, ExportForWebPreference, TransparencyPreference, TransparencyDefaultContainerObject

class StoryPreference(Element):
    """
    The <StoryPreference> element controls the default story preferences for 
    stories in an InDesign document. Values that you specify here will apply to 
    the story preferences of all stories that do not explicitly define these 
    attributes.
    """
    OpticalMarginAlignment = BooleanField()
    OpticalMarginSize = FloatField()
    FrameType = StringField()
    StoryOrientation = StringField()
    StoryDirection = StringField()
    

# TextPreference, TextDefault, DictionaryPreference, AnchoredObjectDefault, AnchoredObjectSetting, BaselineFrameGridOption, FootnoteOption, 


class TextWrapPreferenceProperties(Properties):
    TextWrapOffset = RectangleBoundsField()
    PathGeometry = ListField(EmbeddedDocumentField(GeometryPathType))


class TextWrapPreference(Element):
    """
    The <TextWrapPreference> element controls the default text wrap applied to 
    page items in an InDesign document. Values that you specify here will apply 
    to all text wraps that do not explicitly define these attributes and 
    elements.
    """
    Inverse = BooleanField()
    ApplyToMasterPageOnly = BooleanField()
    TextWrapSide = StringField()
    TextWrapMode = StringField()
    
    Properties = EmbeddedDocumentField(TextWrapPreferenceProperties)
    

class ContourOption(Element):
    ContourType = StringField()
    IncludeInsideEdges = BooleanField()
    ContourPathName = StringField()
    

class DocumentPreferenceProperties(Properties):
    ColumnGuideColor = StringField() # TODO: InDesignUIColorType_TypeDef
    MarginGuideColor = StringField() # TODO: InDesignUIColorType_TypeDef

class DocumentPreference(Element):
    """
    The <DocumentPreference> element contains various preferences for the 
    document.
    
    Document preferences define the basic layout of the document. If you omit 
    some or all of the properties set in the <DocumentPreferences> element, 
    InDesign will apply its application default value to the missing property as 
    it opens the IDML file.
    """
    PageHeight = FloatField()
    PageWidth = FloatField()
    PagesPerDocument = IntField()
    FacingPages = BooleanField()
    DocumentBleedTopOffset = FloatField()
    DocumentBleedBottomOffset = FloatField()
    DocumentBleedInsideOrLeftOffset = FloatField()
    DocumentBleedOutsideOrRightOffset = FloatField()
    DocumentBleedUniformSize = BooleanField()
    SlugTopOffset = FloatField()
    SlugBottomOffset = FloatField()
    SlugInsideOrLeftOffset = FloatField()
    SlugRightOrOutsideOffset = FloatField()
    DocumentSlugUniformSize = BooleanField()
    PreserveLayoutWhenShuffling = BooleanField()
    AllowPageShuffle = BooleanField()
    OverprintBlack = BooleanField()
    ColumnGuideLocked = BooleanField()
    Intent = StringField()
    PageBinding = StringField()
    ColumnDirection = StringField()
    MasterTextFrame = BooleanField()
    SnippetImportUsesOriginalLocation = BooleanField()
    
    Properties = EmbeddedDocumentField(DocumentPreferenceProperties)
    

# TODO: GridPreference, GuidePreference, 

class MarginPreference(Element):
    """
    The <MarginPreference> element controls the default margin and column 
    settings for the pages in a spread. Values that you specify here will apply 
    to the margin preferences of all pages where you have not explicitly defined 
    these attributes and elements.
    """
    ColumnCount = IntField()
    ColumnGutter = FloatField()
    Top = FloatField()
    Bottom = FloatField()
    Left = FloatField()
    Right = FloatField()
    ColumnDirection = StringField()
    ColumnsPositions = SpaceSeparatedListField(FloatField())
    

# TODO: PasteboardPreference, ViewPreference, PrintPreference, PrintBookletOption, PrintBookletPrintPreference, IndexOptions, IndexHeaderSetting, PageItemDefault, 

class FrameFittingOption(Element):
    """
    The <FrameFittingOption> element controls the default fitting behavior for 
    all page items in a document. Values that you specify here will apply to all 
    page items that do not explicitly define these attributes and elements.
    """
    AutoFit = BooleanField()
    LeftCrop = BooleanField()
    TopCrop = BooleanField()
    RightCrop = BooleanField()
    BottomCrop = BooleanField()
    FittingOnEmptyFrame = StringField()
    FittingAlignment = StringField()
    

# TODO: ButtonPreference, TinDocumentDDataObject, LayoutGridDataInformation, StoryGridDataInformation, CjkGridPreference, MojikumiUiPreference, ChapterNumberPreference, 

class Preferences(Element):
    """
    IDML files can contain a number of preferences elements that control both 
    document preferences and various default values. In an IDML package, 
    preferences elements are found in the Preferences.xml file in the Resources 
    folder.
    """
    DOMVersion = StringField(required=True)
    DataMerge = EmbeddedDocumentField(DataMerge)
    DataMergeOption = EmbeddedDocumentField(DataMergeOption)
    StoryPreference = EmbeddedDocumentField(StoryPreference)
    TextWrapPreferenceProperties = EmbeddedDocumentField(
        TextWrapPreferenceProperties
    )
    TextWrapPreference = EmbeddedDocumentField(TextWrapPreference)
    ContourOption = EmbeddedDocumentField(ContourOption)
    DocumentPreferenceProperties = EmbeddedDocumentField(
        DocumentPreferenceProperties
    )
    DocumentPreference = EmbeddedDocumentField(DocumentPreference)
    MarginPreference = EmbeddedDocumentField(MarginPreference)
    FrameFittingOption = EmbeddedDocumentField(FrameFittingOption)


