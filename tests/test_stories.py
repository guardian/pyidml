# -*- coding: utf-8 -*-
from tests import FreshersTest, doc

class StoriesTest(FreshersTest):
    """
    Test files in Stories/ are parsed correctly
    """
    
    def setUp(self):
        super(StoriesTest, self).setUp()
        self.story = doc.get_children('Story')[109]
    
    def test_Story(self):
        self.assertElement(self.story, 'Story',
            Self="u100e",
            AppliedTOCStyle="n",
            TrackChanges=False,
            StoryTitle="$ID/",
            AppliedNamedGrid="n"
        )
    
    def test_StoryPreference(self):
        self.assertElement(self.story.children[0], 'StoryPreference',
            OpticalMarginAlignment=False,
            OpticalMarginSize=12,
            FrameType="TextFrameType",
            StoryOrientation="Horizontal",
            StoryDirection="LeftToRightDirection"
        )
    
    def test_InCopyExportOption(self):
        self.assertElement(self.story.children[1], 'InCopyExportOption',
            IncludeGraphicProxies=True,
            IncludeAllResources=False
        )
    
    def test_ParagraphStyleRange(self):
        self.assertElement(self.story.children[2], 'ParagraphStyleRange',
            AppliedParagraphStyle="ParagraphStyle/Body no indent"
        )
        self.assertEqual(len(self.story.children[2].children), 1)
    
    def test_CharacterStyleRange(self):
        element = self.story.children[2].children[0]
        self.assertElement(element, 'CharacterStyleRange',
            AppliedCharacterStyle="CharacterStyle/$ID/[No character style]"
        )
        self.assertEqual(len(element.children), 2)
        self.assertEqual(unicode(element.children[0]), u"Good writers are the heart and soul of any paper – without them, there would be nothing to print! If you fancy trying your hand at being a journalist or writer, this is where to start.")
        self.assertElement(element.children[1], 'Br')
    
    def test_complex_ParagraphStyleRange(self):
        element = self.story.children[3]
        
        self.assertElement(element.children[0], 'CharacterStyleRange',
            AppliedCharacterStyle="CharacterStyle/$ID/[No character style]"
        )
        self.assertEqual(len(element.children[0].children), 5)
        self.assertEqual(
            unicode(element.children[0].children[0]),
            u"We have several sections to choose from. If you like to keep on top of goings-on, perhaps News would be your thing, while Comment allows you to have your say on campus, national and international issues. To follow some of Warwick’s sports teams, get involved in the back pages, or try your hand at reviews and interviews with Games, Arts, Music, TV, Film and Books. For the economically-minded of you, Money is on hand to offer advice and analysis, or you can offer tips on fashion, food, relationships and more in Lifestyle. Finally, while every section gives you opportunities to write a feature, you could give creating a lengthier, more deeply researched piece a go by getting involved in our Features section."
        )
        self.assertElement(element.children[0].children[1], 'Br')
        self.assertEqual(
            unicode(element.children[0].children[2]),
            u"We’ll give you training and feedback when you join, and you’ll get experience interviewing and writing for print. You never know who you might get to talk to – last year we interviewed the Prime Minister!"
        )
        self.assertElement(element.children[0].children[3], 'Br')
        self.assertEqual(
            unicode(element.children[0].children[4]),
            u"To get started, send an email to the section you’re interested in listed on the left hand side page. If you’re not sure what want to write, email "
        )
        
        self.assertElement(element.children[1], 'CharacterStyleRange',
            AppliedCharacterStyle="CharacterStyle/$ID/[No character style]",
            FontStyle="Italic SmText"
        )
        self.assertEqual(
            unicode(element.children[1].children[0]),
            u"contact@theboar.org"
        )
        
        self.assertElement(element.children[2], 'CharacterStyleRange',
            AppliedCharacterStyle="CharacterStyle/$ID/[No character style]"
        )
        self.assertEqual(
            unicode(element.children[2].children[0]),
            u" or come along to our open day."
        )
    
    
