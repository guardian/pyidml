import numpy
from tests import FreshersTest, doc

class ElementTest(FreshersTest):
    """
    Test element methods
    """
    
    def test_get_document(self):
        self.assertEqual(doc.get_document(), doc)
        self.assertEqual(
            doc.Styles.children[0].get_document(),
            doc
        )

    def test_get_element(self):
        self.assertEqual(
            doc.get_element('Language/$ID/English%3a UK').Self,
            doc.get_children('Language')[0].Self,
        )

    def test_get_transform(self):
        """
        Test get_transform() relative to the pasteboard
        """
        self.assertTrue(numpy.all(doc.get_transform() == numpy.identity(3)))
        spread = doc.get_children('Spread')[1]
        self.assertTrue(numpy.all(
            spread.get_transform() == 
            numpy.matrix([
                [1, 0, 0],
                [0, 1, 0],
                [0, 1200.472440944882, 1],
            ])
        ))
        page_item = spread.get_children('TextFrame')[0]
        self.assertTrue(numpy.all(
            page_item.get_transform() == 
            numpy.matrix([
                [1, 0, 0],
                [0, 1, 0],
                [401.10236220472433, 941.96692913385834, 1],
            ])
        ))

    def test_relative_get_transform(self):
        """
        Test get_transform() relative to other elements
        """
        page_item = doc.get_children('Spread')[1].get_children('TextFrame')[0]
        self.assertTrue(numpy.all(
            page_item.get_transform('Spread') ==
            numpy.matrix([
                [1, 0, 0],
                [0, 1, 0],
                [401.10236220472433, -258.50551181102367, 1],
            ])
        ))
        print page_item.get_transform('TextFrame')
        self.assertTrue(numpy.all(
            page_item.get_transform('TextFrame') == numpy.identity(3)
        ))



