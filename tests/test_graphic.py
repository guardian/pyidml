from tests import FreshersTest, doc

class GraphicTest(FreshersTest):
    """
    Test Graphic.xml is parsed correctly
    """
    
    def setUp(self):
        super(GraphicTest, self).setUp()
        self.graphic = doc.children[2]
    
    def test_graphic(self):
        self.assertEqual(self.graphic.__class__.__name__, 'Graphic')
        self.assertEqual(self.graphic.DOMVersion, '6.0')
    
    def test_color(self):
        self.assertEqual(self.graphic.children[0].__class__.__name__, 'Color')
        self.assertEqual(len(self.graphic.get_children('Color')), 24)
        self.assertProps(self.graphic.children[0], 
            Self='Color/25%25 Black',
            Model='Process',
            Space="CMYK",
            ColorValue=[0, 0, 0, 25],
            ColorOverride='Normal',
            AlternateSpace="NoAlternateColor",
            AlternateColorValue=[],
            Name='25% Black',
            ColorEditable=True,
            ColorRemovable=True,
            Visible=True,
            SwatchCreatorID=7937,
        )
    
    def test_ink(self):
        self.assertEqual(self.graphic.children[24].__class__.__name__, 'Ink')
        self.assertEqual(len(self.graphic.get_children('Ink')), 4)
        self.assertProps(self.graphic.children[24],
            Self='Ink/$ID/Process Cyan',
            Name='$ID/Process Cyan',
            Angle=75,
            ConvertToProcess=False,
            Frequency=70,
            NeutralDensity=0.61,
            PrintInk=True,
            TrapOrder=1,
            InkType='Normal',
        )
    
    def test_pasted_smooth_shade(self):
        self.assertEqual(self.graphic.children[28].__class__.__name__, 'PastedSmoothShade')
        self.assertEqual(len(self.graphic.get_children('PastedSmoothShade')), 1)
        self.assertProps(self.graphic.children[28], 
            Self='PastedSmoothShade/u5f',
            Name='$ID/',
            ContentsVersion=0,
            ContentsType='ConstantShade',
            SpotColorList=[],
            ContentsEncoding='Ascii64Encoding',
            ContentsMatrix=[1, 0, 0, 1, 0, 0],
            ColorEditable=True,
            ColorRemovable=True,
            Visible=False,
            SwatchCreatorID=7937,
        )
        self.assertEqual(
            self.graphic.children[28].Properties.Contents, 
            'AAAAAT/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=='
        )
    
    def test_swatch(self):
        self.assertEqual(self.graphic.children[29].__class__.__name__, 'Swatch')
        self.assertEqual(len(self.graphic.get_children('Swatch')), 1)
        self.assertProps(self.graphic.children[29],
            Self='Swatch/None',
            Name='None',
            ColorEditable=False,
            ColorRemovable=False,
            Visible=True,
            SwatchCreatorID=7937,
        )
    
    def test_gradient(self):
        gradient = self.graphic.children[30]
        self.assertEqual(
            gradient.__class__.__name__,
            'Gradient'
        )
        self.assertEqual(len(self.graphic.get_children('Gradient')), 1)
        self.assertProps(gradient,
            Self="Gradient/u61",
            Type="Linear",
            Name="$ID/",
            ColorEditable=True,
            ColorRemovable=True,
            Visible=False,
            SwatchCreatorID=7937
        )
        
        self.assertEqual(len(gradient.children), 2)
        self.assertEqual(
            gradient.children[0].__class__.__name__,
            'GradientStop'
        )
        self.assertProps(gradient.children[0],
            Self="u61GradientStop0",
            StopColor="Color/u60",
            Location=0
        )
    
    def test_stroke_style(self):
        self.assertEqual(
            self.graphic.children[31].__class__.__name__, 
            'StrokeStyle'
        )
        self.assertEqual(len(self.graphic.get_children('StrokeStyle')), 18)
        self.assertProps(self.graphic.children[31],
            Self="StrokeStyle/$ID/Triple_Stroke",
            Name="$ID/Triple_Stroke"
        )
