# -*- coding: utf-8 -*-
from tests import FreshersTest, doc

class PreferencesTest(FreshersTest):
    """
    Test Resources/Preferences.xml is parsed correctly
    """
    
    def setUp(self):
        super(PreferencesTest, self).setUp()
        self.preferences = doc.Preferences
    
    def test_StoryPreference(self):
        self.assertElement(
            self.preferences.StoryPreference, 
            'StoryPreference',
            OpticalMarginAlignment=False,
            OpticalMarginSize=12,
            FrameType="TextFrameType",
            StoryOrientation="Horizontal",
            StoryDirection="LeftToRightDirection"
        )
    
    def test_DocumentPreference(self):
        self.assertElement(
            self.preferences.DocumentPreference, 
            'DocumentPreference',
            PageHeight=1020.472440944882,
            PageWidth=819.2125984251969,
            PagesPerDocument=1,
            FacingPages=True,
            DocumentBleedTopOffset=0,
            DocumentBleedBottomOffset=0,
            DocumentBleedInsideOrLeftOffset=0, 
            DocumentBleedOutsideOrRightOffset=0,
            DocumentBleedUniformSize=True,
            SlugTopOffset=0,
            SlugBottomOffset=0,
            SlugInsideOrLeftOffset=0,
            SlugRightOrOutsideOffset=0,
            DocumentSlugUniformSize=False,
            PreserveLayoutWhenShuffling=True,
            AllowPageShuffle=True,
            OverprintBlack=True,
            PageBinding="LeftToRight",
            ColumnDirection="Horizontal",
            ColumnGuideLocked=True,
            MasterTextFrame=False,
            SnippetImportUsesOriginalLocation=False
        )
    