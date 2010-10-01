from tests import FreshersTest, doc

class SpreadTest(FreshersTest):
    """
    Test files in Spreads/ are parsed correctly
    """
    
    def setUp(self):
        super(SpreadTest, self).setUp()
        self.spread = doc.get_children('Spread')[0]
    
    def test_count(self):
        self.assertEqual(len(doc.get_children('Spread')), 5)
    
    def test_Spread(self):
        self.assertEqual(self.spread.__class__.__name__, 'Spread')
        self.assertProps(self.spread,
            Self="u1261",
            FlattenerOverride="Default",
            ShowMasterItems=True,
            PageCount=1,
            BindingLocation=0,
            AllowPageShuffle=True,
            ItemTransform=[1, 0, 0, 1, 0, 0],
            PageTransitionType="None",
            PageTransitionDirection="NotApplicable", 
            PageTransitionDuration="Medium"
        )
    
    def test_FlattenerPreference(self):
        element = self.spread.children[0]
        self.assertEqual(element.__class__.__name__, 'FlattenerPreference')
        self.assertProps(element,
            LineArtAndTextResolution=300,
            GradientAndMeshResolution=150,
            ClipComplexRegions=False,
            ConvertAllStrokesToOutlines=False,
            ConvertAllTextToOutlines=False
        )
        self.assertEqual(element.Properties.RasterVectorBalance, 50)
    
    def test_Page(self):
        self.assertEqual(len(self.spread.get_children('Page')), 1)
        element = self.spread.children[1]
        self.assertElement(element, 'Page',
            Self="u1266",
            Name="1",
            AppliedTrapPreset="TrapPreset/$ID/kDefaultTrapStyleName",
            AppliedMaster="n",
            OverrideList=[],
            TabOrder=[],
            GridStartingPoint="TopOutside",
            UseMasterGrid=True
        )
        #self.assertEqual(element.Properties.Descriptor, '') # TODO
        
        self.assertElement(element.children[0], 'MarginPreference',
            ColumnCount=5,
            ColumnGutter=11.999055118110235,
            Top=31.181102362204726,
            Bottom=31.181102362204726,
            Left=25.511811023622048,
            Right=42.51968503937008,
            ColumnDirection="Horizontal",
            ColumnsPositions=[0, 140.63697637795275, 152.63603149606297, 293.2730078740157, 305.27206299212594, 445.9090393700787, 457.9080944881889, 598.5450708661417, 610.544125984252, 751.1811023622047]
        )
        
        self.assertElement(element.children[1], 'GridDataInformation',
            FontStyle="Regular",
            PointSize=12,
            CharacterAki=0,
            LineAki=9,
            HorizontalScale=100,
            VerticalScale=100,
            LineAlignment="LeftOrTopLineJustify",
            GridAlignment="AlignEmCenter",
            CharacterAlignment="AlignEmCenter"
        )
        self.assertEqual(element.children[1].Properties.AppliedFont, 'Times New Roman')
    
    def test_TextFrame(self):
        self.assertEqual(len(self.spread.get_children('TextFrame')), 16)
        
        element = self.spread.children[2]
        self.assertElement(element, 'TextFrame',
            Self="u14d2",
            ParentStory="u14d5",
            PreviousTextFrame="n",
            NextTextFrame="n",
            ContentType="TextType",
            AppliedObjectStyle="ObjectStyle/News text box", 
            GradientFillStart=[-299.27253543307086, 95.05984251968505],
            GradientFillLength=598.5450708661417,
            GradientFillAngle=0,
            GradientStrokeStart=[-299.27253543307086, 95.05984251968505], 
            GradientStrokeLength=598.5450708661417,
            GradientStrokeAngle=0,
            ItemLayer="ua4",
            Locked=False,
            LocalDisplaySetting="Default",
            GradientFillHiliteLength=0,
            GradientFillHiliteAngle=0,
            GradientStrokeHiliteLength=0,
            GradientStrokeHiliteAngle=0,
            ItemTransform=[1, 0, 0, 1, 324.7843464566929, 311.93858267716536]
        )
        
        # Check PathGeometry
        self.assertEqual(element.Properties.PathGeometry[0].PathOpen, False)
        self.assertElement(element.Properties.PathGeometry[0].PathPointArray[0], 
            'PathPointType',
            Anchor=[-299.27253543307086, -95.14488188976377], 
            LeftDirection=[-299.27253543307086, -95.14488188976377], 
            RightDirection=[-299.27253543307086, -95.14488188976377]
        )
        
        # Check TransparencySetting
        self.assertElement(element.children[0], 'TransparencySetting')
        self.assertElement(element.children[0].children[0], 
            'DropShadowSetting',
            KnockedOut=True
        )
        
        # Check TextFramePreference
        self.assertElement(element.children[1], 
            'TextFramePreference',
            TextColumnCount=4,
            TextColumnFixedWidth=140.63626771653543
        )
        
        # Check TextWrapPreference
        self.assertElement(element.children[2], 
            'TextWrapPreference',
            Inverse=False,
            ApplyToMasterPageOnly=False,
            TextWrapSide="BothSides",
            TextWrapMode="None"
        )
        self.assertEqual(element.children[2].Properties.TextWrapOffset, {
            'Top': 0,
            'Left': 0,
            'Bottom': 0,
            'Right': 0
        })
        
    def test_Rectangle(self):
        element = self.spread.children[3]
        self.assertElement(element, 'Rectangle',
            Self="u126f",
            StoryTitle="$ID/",
            ContentType="Unassigned",
            AppliedObjectStyle="ObjectStyle/Dividing line",
            FillTint=9,
            StrokeWeight=0,
            StrokeColor="Swatch/None",
            GradientFillStart=[0, 0],
            GradientFillLength=0,
            GradientFillAngle=0,
            GradientStrokeStart=[0, 0],
            GradientStrokeLength=0,
            GradientStrokeAngle=0,
            ItemLayer="ua4",
            Locked=False,
            LocalDisplaySetting="Default",
            GradientFillHiliteLength=0,
            GradientFillHiliteAngle=0,
            GradientStrokeHiliteLength=0,
            GradientStrokeHiliteAngle=0,
            ItemTransform=[1, 0, 0, 1, 0.1249999999998721, 8.503937007873901]
        )
        
        # Check PathGeometry
        self.assertEqual(element.Properties.PathGeometry[0].PathOpen, False)
        self.assertElement(element.Properties.PathGeometry[0].PathPointArray[0], 
            'PathPointType',
            Anchor=[25.636811023622048, 422.67401574803165], 
            LeftDirection=[25.636811023622048, 422.67401574803165], 
            RightDirection=[25.636811023622048, 422.67401574803165]
        )
        
        # Check InCopyExportOption
        self.assertElement(element.children[2],
            'InCopyExportOption',
            IncludeGraphicProxies=True,
            IncludeAllResources=False
        )
        
        # Check FrameFittingOption
        self.assertElement(element.children[3],
            'FrameFittingOption',
            LeftCrop=0,
            TopCrop=0,
            RightCrop=0,
            BottomCrop=0,
            FittingOnEmptyFrame="None",
            FittingAlignment="TopLeftAnchor"
        )
    
    def test_Image(self):
        element = self.spread.children[4].get_children('Image')[0]
        self.assertElement(element, 'Image',
            Self="u213b",
            Space="$ID/#Links_RGB",
            ActualPpi=[72, 72],
            EffectivePpi=[332, 332],
            ImageRenderingIntent="UseColorSettings", 
            AppliedObjectStyle="ObjectStyle/$ID/[None]", 
            LocalDisplaySetting="Default",
            ImageTypeName="$ID/TIFF",
            ItemTransform=[0.2169934437430858, 0, 0, 0.21699344374308585, -395.25354330708643, -274.7363762608189]
        )
        
        self.assertProps(element.Properties,
            Profile="$ID/None",
            GraphicBounds={
                'Left': 0,
                'Top': 0,
                'Right': 3872,
                'Bottom': 2592
            }
        )
        
        # Check TextWrapPreference
        self.assertElement(element.children[0], 
            'TextWrapPreference',
            Inverse=False,
            ApplyToMasterPageOnly=False,
            TextWrapSide="BothSides",
            TextWrapMode="None"
        )
        self.assertEqual(element.children[0].Properties.TextWrapOffset, {
            'Top': 0,
            'Left': 0,
            'Bottom': 0,
            'Right': 0
        })
        self.assertElement(element.children[0].children[0], 
            'ContourOption',
            ContourType="SameAsClipping",
            IncludeInsideEdges=False,
            ContourPathName="$ID/"
        )
        
        # Check MetadataPacketPreference
        self.assertElement(element.children[1], 'MetadataPacketPreference')
        self.assertTrue(element.children[1].Properties.Contents.startswith(
            '<?xpacket'
        ))
        
        # Check Link
        self.assertElement(element.children[2], 'Link',
            Self="u213f",
            AssetURL="$ID/",
            AssetID="$ID/",
            LinkResourceURI="file:/Users/ben/Documents/Boar/Volume%2033/Issue%200/Images/Rootes_Social_Building_at_University_of_Warwick.tif",
            LinkResourceFormat="$ID/TIFF",
            StoredState="Normal",
            LinkClassID=35906,
            LinkClientID=257,
            LinkResourceModified=False,
            LinkObjectModified=False,
            ShowInUI=True,
            CanEmbed=True,
            CanUnembed=True,
            CanPackage=True,
            ImportPolicy="NoAutoImport",
            ExportPolicy="NoAutoExport",
            LinkImportStamp="file 129276405430000000 8925588", 
            LinkImportModificationTime="2010-08-30T11:15:43", 
            LinkImportTime="2010-08-30T11:16:12",
        )
        
        # Check ClippingPathSettings
        self.assertElement(element.children[3], 'ClippingPathSettings',
            ClippingType="None",
            InvertPath=False,
            IncludeInsideEdges=False,
            RestrictToFrame=False,
            UseHighResolutionImage=True,
            Threshold=25,
            Tolerance=2,
            InsetFrame=0,
            AppliedPathName="$ID/",
            Index=-1
        )
        
        # Check ImageIOPreference
        self.assertElement(element.children[4], 'ImageIOPreference',
            ApplyPhotoshopClippingPath=True,
            AllowAutoEmbedding=True,
            AlphaChannelName="$ID/"
        )
    
    def test_GraphicLine(self):
        element = self.spread.get_children('GraphicLine')[0]
        self.assertElement(element, 'GraphicLine',
            Self="u12e2",
            ContentType="Unassigned",
            AppliedObjectStyle="ObjectStyle/Dividing line",
            GradientFillStart=[0, 0],
            GradientFillLength=0,
            GradientFillAngle=0,
            GradientStrokeStart=[0, 0],
            GradientStrokeLength=0,
            GradientStrokeAngle=0,
            ItemLayer="ua4",
            Locked=False,
            LocalDisplaySetting="Default",
            GradientFillHiliteLength=0,
            GradientFillHiliteAngle=0,
            GradientStrokeHiliteLength=0,
            GradientStrokeHiliteAngle=0,
            ItemTransform=[1, 0, 0, 1, -61.272137795275626, 66.72756217896466]
        )
        self.assertElement(element.Properties.PathGeometry[0],
            'GeometryPathType',
            PathOpen=True
        )
        self.assertElement(element.Properties.PathGeometry[0].PathPointArray[0],
            'PathPointType',
            Anchor=[462.4995, 364.4503905769409],
            LeftDirection=[462.4995, 364.4503905769409],
            RightDirection=[462.4995, 364.4503905769409]
        )
        
        self.assertElement(element.children[0].children[0],
            'DropShadowSetting',
            KnockedOut=True
        )
        
        self.assertElement(element.children[1], 'TextWrapPreference', 
            Inverse=False,
            ApplyToMasterPageOnly=True,
            TextWrapSide="BothSides",
            TextWrapMode="None"
        )
        self.assertEqual(element.children[1].Properties.TextWrapOffset, {
            'Top': 0,
            'Left': 0,
            'Bottom': 0,
            'Right': 0
        })
        
    def test_PDF(self):
        element = self.spread.get_children('Rectangle')[3].get_children('PDF')[0]
        self.assertElement(element, 'PDF',
            Self="u1301",
            GrayVectorPolicy="IgnoreAll",
            RGBVectorPolicy="IgnoreAll",
            CMYKVectorPolicy="IgnoreAll", 
            AppliedObjectStyle="ObjectStyle/$ID/[None]", 
            LocalDisplaySetting="Default",
            ImageTypeName="$ID/Adobe Portable Document Format (PDF)", 
            ItemTransform=[0.05655866557515179, 0, 0, 0.05655866557515178, -272.92794057023787, 193.11138907173793]
        )
        self.assertEqual(element.Properties.GraphicBounds, {
            'Top': 680.2579956054688,
            'Left': 2.156005859375,
            'Bottom': 1221.051025390625,
            'Right': 547.7680053710938
        })
        
        # Check TextWrapPreference
        self.assertElement(element.children[0], 'TextWrapPreference',        
            Inverse=False,
            ApplyToMasterPageOnly=False,
            TextWrapSide="BothSides",
            TextWrapMode="None"
        )
        self.assertEqual(element.children[0].Properties.TextWrapOffset, {
            'Top': 0,
            'Left': 0,
            'Bottom': 0,
            'Right': 0
        })
        self.assertElement(element.children[0].children[0], 'ContourOption',
            ContourType="SameAsClipping",
            IncludeInsideEdges=False,
            ContourPathName="$ID/"
        )
        
        # Check PDFAttribute
        self.assertElement(element.children[1], 'PDFAttribute',
            PageNumber=1,
            PDFCrop="CropContent",
            TransparentBackground=True
        )
        
        # Check MetadataPacketPreference
        self.assertElement(element.children[2], 'MetadataPacketPreference')
        self.assertTrue(
            element.children[2].Properties.Contents.startswith('<?xpacket')
        )
        
        # Check Link
        self.assertElement(element.children[3], 'Link',
            Self="u1305",
            AssetURL="$ID/",
            AssetID="$ID/",
            LinkResourceURI="file:/Users/ben/Documents/Boar/Volume%2033/Issue%200/Global/Graphics/Recycling_symbol2.ai",
            LinkResourceFormat="$ID/Adobe Portable Document Format (PDF)", 
            StoredState="Normal",
            LinkClassID=35906,
            LinkClientID=257,
            LinkResourceModified=False,
            LinkObjectModified=False,
            ShowInUI=True,
            CanEmbed=True,
            CanUnembed=True,
            CanPackage=True,
            ImportPolicy="NoAutoImport",
            ExportPolicy="NoAutoExport",
            LinkImportStamp="file 129158107480000000 62527", 
            LinkImportModificationTime="2010-04-15T13:12:28", 
            LinkImportTime="2010-08-19T18:16:27"
        )
        
        # Check ClippingPathSettings
        self.assertElement(element.children[4], 'ClippingPathSettings',
            ClippingType="None",
            InvertPath=False,
            IncludeInsideEdges=False,
            RestrictToFrame=False,
            UseHighResolutionImage=True,
            Threshold=25,
            Tolerance=2,
            InsetFrame=0,
            AppliedPathName="$ID/",
            Index=-1
        )
        
        # Check ClippingPathSettings
        self.assertElement(element.children[5], 'GraphicLayerOption',
            UpdateLinkOption="ApplicationSettings"
        )
    
    def test_Group(self):
        element = self.spread.get_children('Group')[0]
        self.assertElement(element, 'Group',
            Self="u1321",
            AppliedObjectStyle="ObjectStyle/$ID/[None]",
            GradientFillStart=[0, 0],
            GradientFillLength=0,
            GradientFillAngle=0,
            GradientStrokeStart=[0, 0],
            GradientStrokeLength=0,
            GradientStrokeAngle=0,
            ItemLayer="ua4",
            Locked=False,
            LocalDisplaySetting="Default",
            GradientFillHiliteLength=0,
            GradientFillHiliteAngle=0,
            GradientStrokeHiliteLength=0,
            GradientStrokeHiliteAngle=0,
            ItemTransform=[1, 0, 0, 1, 319.918109851747, 524.5795244352084]
        )
    
    def test_MasterSpread(self):
        element = doc.get_children('MasterSpread')[12]
        self.assertElement(element, 'MasterSpread',
            Self="u481",
            ItemTransform=[1, 0, 0, 1, 0, 0],
            Name="B-Travel",
            NamePrefix="B",
            BaseName="Travel",
            ShowMasterItems=True,
            PageCount=2,
            OverriddenPageItemProps=""
        )
    
