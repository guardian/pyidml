# -*- coding: utf-8 -*-
from tests import FreshersTest, doc

class DocumentTest(FreshersTest):
    """
    Test designmap.xml is parsed correctly
    """
    
    def test_Document(self):
        self.assertElement(doc, 'Document',
            DOMVersion="6.0",
            Self="d",
            ActiveProcess=None,
            TransparencyAttributeDefaultProperty=None,
            StoryList=[u'u36d', u'u39c', u'u435', u'u463', u'u49a', u'u4b0', u'u4ca', u'u4e0', u'u507', u'u51d', u'u541', u'u557', u'u57b', u'u591', u'u5b6', u'u5cc', u'u5f0', u'u606', u'u62a', u'u640', u'u667', u'u67d', u'u69e', u'u6b4', u'u6d5', u'u6eb', u'u714', u'u72a', u'u74f', u'u765', u'u79d', u'u7b5', u'u7cd', u'u7e5', u'u8ab', u'u8cd', u'ua2f', u'uc4e', u'udbe', u'udd6', u'udef', u'ue3b', u'ue85', u'uea2', u'uec0', u'ued9', u'uef3', u'uf34', u'uf4b', u'uf66', u'uf99', u'ufc9', u'ufe1', u'u100e', u'u1038', u'u1052', u'u1075', u'u108e', u'u10ac', u'u10c5', u'u113d', u'u1180', u'u11ea', u'u123a', u'u127b', u'u129a', u'u12b3', u'u12cc', u'u12e8', u'u130b', u'u1326', u'u1346', u'u135f', u'u1378', u'u13ce', u'u13ee', u'u1408', u'u1421', u'u143a', u'u1453', u'u1478', u'u1491', u'u14b6', u'u14d5', u'u153e', u'u1557', u'u159e', u'u15ba', u'u15d5', u'u15f4', u'u1610', u'u1629', u'u1649', u'u1666', u'u167f', u'u16a2', u'u16be', u'u16da', u'u16f6', u'u170f', u'u172c', u'u1748', u'u1765', u'u177e', u'u17a0', u'u17bc', u'u17f5', u'u1814', u'u1830', u'u184a', u'u1867', u'u19ea', u'u1a0c', u'u1a26', u'u1a3f', u'u1a58', u'u1a72', u'u1a90', u'u1aa9', u'u1ac8', u'u1ae5', u'u1b00', u'u1b35', u'u1b54', u'u1b6e', u'u1ba6', u'u1bc6', u'u1be3', u'u1c16', u'u1c36', u'u1c52', u'u1c6e', u'u1c90', u'u1cb6', u'u1cd2', u'u1cef', u'u1d2d', u'u1d47', u'u1d65', u'u1dbc', u'u1dd7', u'u1dfe', u'u1e1a', u'u1e3c', u'u1e56', u'u1e71', u'u1e8c', u'u1eb1', u'u1ed9', u'u1ef3', u'u1f0f', u'u1f2f', u'u1f4a', u'u1f67', u'u1fc3', u'u1fde', u'u201a', u'u2040', u'u2063', u'u2080', u'u20ab', u'u20cd', u'u20f6', u'u75'],
            FullName=None,
            Name=None,
            Visible=None,
            FilePath=None,
            Modified=None,
            Saved=None,
            ZeroPoint=[0, 0],
            ActiveLayer='ua4',
            UnusedSwatches=[],
            Converted=None,
            Recovered=None,
            ReadOnly=None,
            CMYKProfileList=[],
            RGBProfileList=[],
            CMYKProfile='ISOnewspaper26v4',
            RGBProfile='ColorMatch RGB',
            SolidColorIntent='UseColorSettings',
            AfterBlendingIntent='UseColorSettings',
            DefaultImageIntent='UseColorSettings',
            RGBPolicy='ColorPolicyOff',
            CMYKPolicy='ColorPolicyOff',
            AccurateLABSpots=False,
        )
    
    def test_normalization(self):
        """
        Test idPkg references are imported correctly
        """
        self.assertElement(doc.Graphic, 'Graphic')
        self.assertFalse(hasattr(doc.Graphic, 'src'))
    
    
    def test_Language(self):
        self.assertElement(doc.children[0], 'Language',
            Self='Language/$ID/English%3a UK',
            Name='$ID/English: UK',
            #SingleQuotes="‘’",
            #DoubleQuotes="“”",
            PrimaryLanguageName="$ID/English",
            SublanguageName="$ID/UK",
            Id=525,
            HyphenationVendor="Proximity",
            SpellingVendor="Proximity",
        )
    
        self.assertElement(doc.children[1], 'Language',
            Self='Language/$ID/English%3a USA',
            Name='$ID/English: USA',
            # FIXME
            #SingleQuotes="‘’",
            #DoubleQuotes="“”",
            PrimaryLanguageName="$ID/English",
            SublanguageName="$ID/USA",
            Id=269,
            HyphenationVendor="Proximity",
            SpellingVendor="Proximity",
        )
    
    def test_MojikumiTable(self):
        self.assertElement(doc.children[2], 'MojikumiTable',
            Self="MojikumiTable/$ID/kMojikumiDefaultName15",
            Name="$ID/kMojikumiDefaultName15"
        )
    
    def test_NumberingList(self):
        element = doc.get_children('NumberingList')[0]
        self.assertElement(element, 'NumberingList',
            Self="NumberingList/$ID/[Default]",
            Name="$ID/[Default]",
            ContinueNumbersAcrossStories=False,
            ContinueNumbersAcrossDocuments=False
        )
    
    def test_NamedGrid(self):
        element = doc.get_children('NamedGrid')[0]
        self.assertElement(element, 'NamedGrid',
            Self="NamedGrid/$ID/[Page Grid]",
            Name="$ID/[Page Grid]"
        )
        self.assertEqual(len(element.children), 1)
        
        self.assertElement(element.children[0], 'GridDataInformation',
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
        self.assertProps(element.children[0].Properties,
            AppliedFont="Times New Roman"
        )
    
    def test_MetadataPacketPreference(self):
        element = doc.get_children('MetadataPacketPreference')[0]
        self.assertElement(element, 'MetadataPacketPreference')
        self.assertTrue(element.Properties.Contents.startswith('<?xpacket'))
        
    def test_ConditionalTextPreference(self):
        element = doc.get_children('ConditionalTextPreference')[0]
        self.assertElement(element, 'ConditionalTextPreference',
            ShowConditionIndicators="ShowIndicators",
            ActiveConditionSet="n"
        )
    
    def test_Layer(self):
        element = doc.get_children('Layer')[0]
        self.assertElement(element, 'Layer',
            Self="ua4",
            Name="Layer 1",
            Visible=True,
            Locked=False,
            IgnoreWrap=False,
            ShowGuides=True,
            LockGuides=False,
            UI=True,
            Expendable=True,
            Printable=True
        )
        self.assertEqual(element.Properties.LayerColor, 'LightBlue')
    
    # TODO: DocumentUser, CrossReferenceFormat, IndexingSortOption
    
    def test_ABullet(self):
        self.assertEqual(len(doc.get_children('ABullet')), 6)
        element = doc.get_children('ABullet')[0]
        self.assertElement(element, 'ABullet',
            Self="dABullet0",
            CharacterType="UnicodeOnly",
            CharacterValue=8226
        )
        self.assertProps(element.Properties,
            BulletsFont='$ID/',
            BulletsFontStyle='$ID/'
        )
    
    def test_Assignment(self):
        self.assertEqual(len(doc.get_children('Assignment')), 1)
        element = doc.get_children('Assignment')[0]
        self.assertElement(element, 'Assignment',
            Self="u94",
            Name="$ID/UnassignedInCopy",
            UserName="$ID/", 
            ExportOptions="AssignedSpreads",
            IncludeLinksWhenPackage=True,
            FilePath="$ID/"
        )
        self.assertEqual(element.Properties.FrameColor, 'Nothing')
        
