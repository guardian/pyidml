from pyidml.fields import *
from pyidml.models import Element, Properties
from xml.etree import ElementTree

class LeadingField(FloatField):
    def to_python(self, value):
        if isinstance(value, ElementTree._ElementInterface):
            return value.text
        else:
            return super(LeadingField, self).to_python(value)
    

class TextElementProperties(Properties):
    AllGREPStyles = StringField() # TODO: ListItem
    AllLineStyles = StringField() # TODO: ListItem
    AllNestedStyles = StringField() # TODO: ListItem
    AppliedFont = StringField()
    AppliedNumberingList = StringField()
    BalanceRaggedLines = StringField() # TODO: boolean or BalanceLinesStyle_EnumValue
    BulletChar = StringField() # TODO: undefined
    BulletsCharacterStyle = StringField()
    BulletsFont = StringField()
    BulletsFontStyle = StringField()
    CustomGlyph = StringField()
    KentenFillColor = StringField()
    KentenFont = StringField()
    KentenFontStyle = StringField()
    KentenStrokeColor = StringField()
    KinsokuSet = StringField()
    Leading = LeadingField()
    Mojikumi = StringField()
    NumberingCharacterStyle = StringField()
    NumberingFormat = StringField()
    NumberingRestartPolicies = StringField() # TODO: undefined
    OpenTypeFeatures = StringField() # TODO: ListItem
    RubyFill = StringField()
    RubyFont = StringField()
    RubyFontStyle = StringField()
    RubyStroke = StringField()
    RuleAboveColor = StringField()
    RuleAboveGapColor = StringField()
    RuleAboveType = StringField()
    RuleBelowColor = StringField()
    RuleBelowGapColor = StringField()
    RuleBelowType = StringField()
    StrikeThroughColor = StringField()
    StrikeThroughGapColor = StringField()
    StrikeThroughType = StringField()
    TabList = StringField() # TODO: ListItem
    UnderlineColor = StringField()
    UnderlineGapColor = StringField()
    UnderlineType = StringField()
    

class BaseTextElement(Element):
    """
    Common text properties
    
    Just as all text objects in the InDesign scripting DOM share a large number 
    of properties, all text elements in an IDML package share a large set of 
    common attributes and elements. These attributes and properties can appear 
    in a <Story>, <ParagraphStyleRange>, or <CharacterStyleRange> element 
    inside a <Story> element, and in a <ParagraphStyle> or <CharacterStyle> 
    elements.
    """
    Self = StringField(required=True)
    AllowArbitraryHyphenation = BooleanField()
    AppliedCharacterStyle = StringField()
    AppliedConditions = SpaceSeparatedListField(StringField())
    AppliedLanguage = StringField()
    AppliedParagraphStyle = StringField()
    AutoLeading = FloatField()
    AutoTcy = IntField()
    AutoTcyIncludeRoman = BooleanField()
    BaselineShift = FloatField()
    BulletsAlignment = StringField()
    BulletsAndNumberingListType = StringField()
    BulletsTextAfter = StringField()
    BunriKinshi = BooleanField()
    Capitalization = StringField()
    CharacterAlignment = StringField()
    CharacterDirection = StringField()
    CharacterRotation = FloatField()
    CjkGridTracking = BooleanField()
    Composer = StringField()
    DesiredGlyphScaling = StringField()
    DesiredLetterSpacing = StringField()
    DesiredWordSpacing = StringField()
    DiacriticPosition = StringField()
    DigitsType = StringField()
    DropCapCharacters = IntField()
    DropCapLines = IntField()
    DropcapDetail = IntField()
    EndJoin = StringField()
    FillColor = StringField()
    FillTint = FloatField()
    FirstLineIndent = FloatField()
    FontStyle = StringField()
    GlyphForm = StringField()
    GotoNextX = StringField()
    GradientFillAngle = FloatField()
    GradientFillLength = FloatField()
    GradientFillStart = SpaceSeparatedListField(FloatField())
    GradientStrokeAngle = FloatField()
    GradientStrokeLength = FloatField()
    GradientStrokeStart = SpaceSeparatedListField(FloatField())
    GridAlignFirstLineOnly = BooleanField()
    GridAlignment = StringField()
    GridGyoudori = IntField()
    HorizontalScale = FloatField()
    HyphenWeight = IntField()
    HyphenateAcrossColumns = BooleanField()
    HyphenateAfterFirst = IntField()
    HyphenateBeforeLast = IntField()
    HyphenateCapitalizedWords = BooleanField()
    HyphenateLadderLimit = IntField()
    HyphenateLastWord = BooleanField()
    HyphenateWordsLongerThan = IntField()
    Hyphenation = BooleanField()
    HyphenationZone = FloatField()
    IgnoreEdgeAlignment = BooleanField()
    Jidori = IntField()
    Justification = StringField()
    Kashidas = StringField()
    KeepAllLinesTogether = BooleanField()
    KeepFirstLines = IntField()
    KeepLastLines = IntField()
    KeepLinesTogether = BooleanField()
    KeepRuleAboveInFrame = BooleanField()
    KeepWithNext = IntField()
    KeepWithPrevious = BooleanField()
    KentenAlignment = StringField()
    KentenCharacterSet = StringField()
    KentenCustomCharacter = StringField()
    KentenFontSize = FloatField()
    KentenKind = StringField()
    KentenOverprintFill = StringField()
    KentenOverprintStroke = StringField()
    KentenPlacement = FloatField()
    KentenPosition = StringField()
    KentenStrokeTint = FloatField()
    KentenTint = FloatField()
    KentenWeight = FloatField()
    KentenXScale = FloatField()
    KentenYScale = FloatField()
    KerningMethod = StringField()
    KerningValue = FloatField()
    KeyboardDirection = StringField()
    KinsokuHangType = StringField()
    KinsokuType = StringField()
    LastLineIndent = FloatField()
    LeadingAki = FloatField()
    LeadingModel = StringField()
    LeftIndent = FloatField()
    Ligatures = BooleanField()
    MaximumGlyphScaling = FloatField()
    MaximumLetterSpacing = FloatField()
    MaximumWordSpacing = FloatField()
    MinimumGlyphScaling = FloatField()
    MinimumLetterSpacing = FloatField()
    MinimumWordSpacing = FloatField()
    MiterLimit = FloatField()
    NoBreak = BooleanField()
    NumberingAlignment = StringField()
    NumberingAlignment = BooleanField()
    NumberingContinue = BooleanField()
    NumberingExpression = StringField()
    NumberingLevel = IntField()
    NumberingStartAt = IntField()
    NumberingApplyRestartPolicy = BooleanField()
    OTFContextualAlternate = BooleanField()
    OTFDiscretionaryLigature = BooleanField()
    OTFFigureStyle = StringField()
    OTFFraction = BooleanField()
    OTFHVKana = BooleanField()
    OTFHistorical = BooleanField()
    OTFJustificationAlternate = BooleanField()
    OTFLocale = BooleanField()
    OTFMark = BooleanField()
    OTFOrdinal = BooleanField()
    OTFOverlapSwash = BooleanField()
    OTFProportionalMetrics = BooleanField()
    OTFRomanItalics = BooleanField()
    OTFSlashedZero = BooleanField()
    OTFStretchedAlternate = BooleanField()
    OTFStylisticAlternate = BooleanField()
    OTFStylisticSets = IntField()
    OTFSwash = BooleanField()
    OTFTitling = BooleanField()
    OverprintFill = BooleanField()
    OverprintStroke = BooleanField()
    ParagraphBreakType = StringField()
    PageNumberType = StringField()
    ParagraphDirection = StringField()
    ParagraphGyoudori = BooleanField()
    ParagraphJustification = StringField()
    PointSize = FloatField()
    Position = StringField()
    PositionalForm = StringField()
    Rensuuji = BooleanField()
    RightIndent = FloatField()
    RotateSingleByteCharacters = BooleanField()
    RubyAlignment = StringField()
    RubyAutoAlign = BooleanField()
    RubyAutoScaling = BooleanField()
    RubyAutoTcyAutoScale = BooleanField()
    RubyAutoTcyDigits = IntField()
    RubyAutoTcyIncludeRoman = BooleanField()
    RubyFlag = IntField()
    RubyFontSize = FloatField()
    RubyOpenTypePro = BooleanField()
    RubyOverhang = BooleanField()
    RubyOverprintFill = StringField()
    RubyOverprintStroke = StringField()
    RubyParentOverhangAmount = StringField()
    RubyParentScalingPercent = FloatField()
    RubyParentSpacing = StringField()
    RubyPosition = StringField()
    RubyString = StringField()
    RubyStrokeTint = FloatField()
    RubyTint = FloatField()
    RubyType = StringField()
    RubyWeight = FloatField()
    RubyXOffset = FloatField()
    RubyXScale = FloatField()
    RubyYOffset = FloatField()
    RubyYScale = FloatField()
    RuleAbove = BooleanField()
    RuleAboveGapOverprint = BooleanField()
    RuleAboveGapTint = FloatField()
    RuleAboveLeftIndent = FloatField()
    RuleAboveLineWeight = FloatField()
    RuleAboveOffset = FloatField()
    RuleAboveOverprint = BooleanField()
    RuleAboveRightIndent = FloatField()
    RuleAboveTint = FloatField()
    RuleAboveWidth = StringField()
    RuleBelow = BooleanField()
    RuleBelowGapOverprint = BooleanField()
    RuleBelowGapTint = FloatField()
    RuleBelowLeftIndent = FloatField()
    RuleBelowLineWeight = FloatField()
    RuleBelowOffset = FloatField()
    RuleBelowOverprint = BooleanField()
    RuleBelowRightIndent = FloatField()
    RuleBelowTint = FloatField()
    RuleBelowWidth = StringField()
    ScaleAffectsLineHeight = BooleanField()
    ShataiAdjustRotation = BooleanField()
    ShataiAdjustTsume = BooleanField()
    ShataiDegreeAngle = FloatField()
    ShataiMagnification = FloatField()
    SingleWordJustification = StringField()
    Skew = FloatField()
    SpaceAfter = FloatField()
    SpaceBefore = FloatField()
    SpanColumnInsideGutter = FloatField()
    SpanColumnOutsideGutter = FloatField()
    SpanColumnType = StringField()
    SpanSplitColumnCount = IntField()
    StartParagraph = StringField()
    StrikeThroughGapOverprint = BooleanField()
    StrikeThroughGapTint = FloatField()
    StrikeThroughOffset = FloatField()
    StrikeThroughOverprint = BooleanField()
    StrikeThroughTint = FloatField()
    StrikeThroughWeight = FloatField()
    StrikeThru = BooleanField()
    StrokeAlignment = StringField()
    StrokeColor = StringField()
    StrokeTint = FloatField()
    StrokeWeight = FloatField()
    Tatechuyoko = BooleanField()
    TatechuyokoXOffset = FloatField()
    TatechuyokoYOffset = FloatField()
    Tracking = FloatField()
    TrailingAki = FloatField()
    TreatIdeographicSpaceAsSpace = BooleanField()
    Tsume = FloatField()
    Underline = BooleanField()
    UnderlineGapOverprint = BooleanField()
    UnderlineGapTint = FloatField()
    UnderlineOffset = FloatField()
    UnderlineOverprint = BooleanField()
    UnderlineTint = FloatField()
    UnderlineWeight = FloatField()
    VerticalScale = FloatField()
    Warichu = BooleanField()
    WarichuAlignment = StringField()
    WarichuCharsAfterBreak = IntField()
    WarichuCharsBeforeBreak = IntField()
    WarichuLineSpacing = FloatField()
    WarichuLines = IntField()
    WarichuSize = FloatField()
    XOffsetDiacritic = FloatField()
    YOffsetDiacritic = FloatField()
    
    Properties = EmbeddedDocumentField(TextElementProperties)
    

class StoryProperties(TextElementProperties):
    ExcelImportPreferences = StringField() # TODO: ListItem
    StyleMappingPreferences = StringField() # TODO: ListItem
    TextImportPreferences = StringField() # TODO: ListItem
    WordRTFImportPreferences = StringField() # TODO: ListItem
    

class Story(BaseTextElement):
    """
    A story, or "text flow" is the basic text container in an InDesign document; 
    all text exists inside stories. Stories are associated with at least one 
    text frame or text path, and can span any number of linked text frames or 
    text paths in a document.
    
    In an IDML package, the XML documents representing stories are stored inside 
    the "Stories". Each file contains a single <Story> element. The root element 
    of a Story.xml file is the <Story> element, and each story file stores 
    contains a single <Story> element.
    
    The <Story> element is very complex. The schema of <Story> element describes 
    more than 200 simple attributes and more than 40 complex attributes that can 
    appear in the <Properties> element of the story. In addition, the <Story> 
    element can contain other child elements, including elements corresponding 
    to inline or anchored frames, tables, notes, hyperlinks, and footnotes.

    That said, most of these attributes and elements of story are optional. You 
    do not need to construct all of them to assemble a new story for use in an 
    IDML package.
    """
    AppliedNamedGrid = StringField()
    AppliedTOCStyle = StringField()
    StoryTitle = StringField()
    TrackChanges = BooleanField()
    
    Properties = EmbeddedDocumentField(StoryProperties)
    
    @classmethod
    def from_xml(cls, e):
        if e[0] and e[0].tag == 'Story':
            e = e[0]
        return super(Story, cls).from_xml(e)
    

class ParagraphStyleRange(BaseTextElement):
    """
    Text range elements are the XML elements that define a range of text in a 
    story. In general, a text range element contains a continuous "run" of text 
    formatting.
    
    These objects are further broken up into <ParagraphStyleRange> elements, 
    which contain ranges of continuous paragraph formatting.
    """
    

class CharacterStyleRange(BaseTextElement):
    """
    Inside a <ParagraphStyleRange> element, you'll find one or more 
    <CharacterStyleRange> elements. <CharacterStyleRange> elements represent a 
    continuous run of text formatting.
    """
    

class Content(Element):
    def __unicode__(self):
        return self.text
    
    @classmethod
    def from_xml(cls, e):
        instance = cls()
        instance.text = e.text
        return instance

class Br(Element):
    pass

# TODO: Tables
# TODO: Notes


class AnchoredObjectSetting(Element):
    """
    InDesign documents often feature page items that have been embedded in text. 
    These frames move with the text as the composition and layout of the text 
    changes. These embedded frames are referred to as anchored frames. Anchored 
    frames are also sometimes called inline frames - in IDML, an inline frame is 
    a special case of an anchored frame.
    """
    AnchoredPosition = StringField()
    SpineRelative = BooleanField()
    LockPosition = BooleanField()
    PinPosition = BooleanField()
    AnchorPoint = StringField()
    HorizontalAlignment = StringField()
    HorizontalReferencePoint = StringField()
    VerticalAlignment = StringField()
    VerticalReferencePoint = StringField()
    AnchorXoffset = FloatField()
    AnchorYoffset = FloatField()
    AnchorSpaceAbove = FloatField()
    

class HyperlinkTextSource(Element):
    """
    Hyperlink text sources differ from other inline elements as they appear as 
    child elements of a <CharacterStyleRange>, and contain a <Content> element. 
    Other inline elements appear as siblings of the <Content> element of the 
    <CharacterStyleRange>.
    """
    Self = StringField(required=True)
    Name = StringField()
    Hidden = BooleanField()
    AppliedCharacterStyle = StringField()
    
    Properties = EmbeddedDocumentField(Properties)
    

class HyperlinkTextDestination(Element):
    """
    A hyperlink text destinations is one of the possible "targets" of a 
    hyperlink.
    """
    Self = StringField(required=True)
    Name = StringField(required=True)
    Hidden = BooleanField()
    DestinationUniqueKey = IntField()
    
    Properties = EmbeddedDocumentField(Properties)
    

class CrossReferenceSource(Element):
    """
    A <CrossReferenceSource> is the source for a cross reference hyperlink.
    
    (new in 7.0)
    """
    Self = StringField(required=True)
    AppliedFormat = StringField(required=True)
    Name = StringField()
    Hidden = BooleanField()
    AppliedCharacterStyle = StringField()
    
    Properties = EmbeddedDocumentField(Properties)
    

