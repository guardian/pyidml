from pyidml.fields import *
from pyidml.models import Element, Properties

class Preferences(Element):
    """
    IDML files can contain a number of preferences elements that control both 
    document preferences and various default values. In an IDML package, 
    preferences elements are found in the Preferences.xml file in the Resources 
    folder.
    """
    DOMVersion = StringField(required=True)
    
    

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
    

# TODO: LayoutAdjustmentPreference, XMLImportPeference, XMLExportPreference, XMLPreference, ExportForWebPreference, TransparencyPreference, TransparencyDefaultContainerObject, StoryPreference, TextPreference, TextDefault, DictionaryPreference, AnchoredObjectDefault, AnchoredObjectSetting, BaselineFrameGridOption, FootnoteOption, TextWrapPreference, ContourOption, 

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
    

# TODO: PasteboardPreference, ViewPreference, PrintPreference, PrintBookletOption, PrintBookletPrintPreference, IndexOptions, IndexHeaderSetting, PageItemDefault, FrameFittingOption, ButtonPreference, TinDocumentDDataObject, LayoutGridDataInformation, StoryGridDataInformation, CjkGridPreference, MojikumiUiPreference, ChapterNumberPreference, 



