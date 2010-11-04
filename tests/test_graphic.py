from tests import FreshersTest, doc

class GraphicTest(FreshersTest):
    """
    Test Graphic.xml is parsed correctly
    """
    
    def setUp(self):
        super(GraphicTest, self).setUp()
        self.graphic = doc.Graphic
    
    def test_Graphic(self):
        self.assertElement(self.graphic, 'Graphic',
            DOMVersion='6.0'
        )
    
    def test_Color(self):
        self.assertElement(self.graphic.children[0], 'Color',
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
        self.assertEqual(len(self.graphic.get_children('Color')), 24)
    
    def test_Ink(self):
        self.assertElement(self.graphic.children[24], 'Ink',
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
        self.assertEqual(len(self.graphic.get_children('Ink')), 4)
    
    def test_PastedSmoothShade(self):
        self.assertElement(self.graphic.children[28], 'PastedSmoothShade',
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
        self.assertEqual(len(self.graphic.get_children('PastedSmoothShade')), 1)
        self.assertEqual(
            self.graphic.children[28].Properties.Contents, 
            'AAAAAT/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=='
        )
    
    def test_Swatch(self):
        self.assertElement(self.graphic.children[29], 'Swatch',
            Self='Swatch/None',
            Name='None',
            ColorEditable=False,
            ColorRemovable=False,
            Visible=True,
            SwatchCreatorID=7937,
        )
        self.assertEqual(len(self.graphic.get_children('Swatch')), 1)
    
    def test_Gradient(self):
        gradient = self.graphic.children[30]
        self.assertElement(gradient, 'Gradient',
            Self="Gradient/u61",
            Type="Linear",
            Name="$ID/",
            ColorEditable=True,
            ColorRemovable=True,
            Visible=False,
            SwatchCreatorID=7937
        )
        self.assertEqual(len(self.graphic.get_children('Gradient')), 1)
        
        self.assertEqual(len(gradient.children), 2)
        self.assertElement(gradient.children[0], 'GradientStop',
            Self="u61GradientStop0",
            StopColor__Self="Color/u60",
            Location=0
        )
    
    def test_StrokeStyle(self):
        self.assertElement(self.graphic.children[31], 'StrokeStyle',
            Self="StrokeStyle/$ID/Triple_Stroke",
            Name="$ID/Triple_Stroke"
        )
        self.assertEqual(len(self.graphic.get_children('StrokeStyle')), 18)


