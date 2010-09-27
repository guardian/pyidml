from tests import FreshersTest

class FontsTest(FreshersTest):
    """
    Test Fonts.xml is parsed correctly
    """
    
    def setUp(self):
        super(FontsTest, self).setUp()
        self.fonts = self.doc.children[3]
    
    def test_fonts(self):
        self.assertEqual(self.fonts.__class__.__name__, 'Fonts')
        self.assertEqual(self.fonts.DOMVersion, '6.0')
    
    def test_font_family(self):
        self.assertEqual(
            self.fonts.children[0].__class__.__name__, 
            'FontFamily'
        )
        self.assertEqual(len(self.fonts.get_children('FontFamily')), 8)
        self.assertProps(self.fonts.children[0], 
            Self="di6a",
            Name="Myriad Pro"
        )
    
    def test_font(self):
        font_family = self.fonts.children[0]
        self.assertEqual(
            font_family.children[0].__class__.__name__, 
            'Font'
        )
        self.assertEqual(len(font_family.get_children('Font')), 20)
        self.assertProps(font_family.children[0], 
            Self="di6aFontnMyriad Pro Light Condensed",
            FontFamily="Myriad Pro",
            Name="Myriad Pro Light Condensed",
            PostScriptName="MyriadPro-LightCond",
            Status="Substituted",
            FontStyleName="Light Condensed",
            FontType="OpenTypeCFF",
            WritingScript=0,
            FullName="Myriad Pro Light Condensed",
            FullNameNative="Myriad Pro Light Condensed",
            FontStyleNameNative="$ID/Light Condensed",
            PlatformName="$ID/",
            Version="Version 2.006;PS 002.000;Core 1.0.38;makeotf.lib1.6.6565",
        )
    
    def test_composite_font(self):
        composite_font = self.fonts.get_children('CompositeFont')[0]
        self.assertEqual(
            composite_font.__class__.__name__, 
            'CompositeFont'
        )
        self.assertEqual(len(self.fonts.get_children('CompositeFont')), 1)
        self.assertProps(composite_font, 
            Self="CompositeFont/$ID/[No composite font]",
            Name="$ID/[No composite font]"
        )
        
    def test_composite_font_entry(self):
        composite_font = self.fonts.get_children('CompositeFont')[0]
        self.assertEqual(
            composite_font.children[0].__class__.__name__, 
            'CompositeFontEntry'
        )
        self.assertEqual(len(composite_font.get_children('CompositeFontEntry')), 6)
        self.assertProps(composite_font.children[0],
            Self="u6e",
            Name="$ID/Kanji",
            FontStyle="$ID/R",
            RelativeSize=100,
            HorizontalScale=100,
            VerticalScale=100,
            Locked=True,
            ScaleOption=True,
            BaselineShift=0
        )
        self.assertEqual(
            composite_font.children[0].Properties['AppliedFont'],
            'Kozuka Mincho Pro'
        )
        
    