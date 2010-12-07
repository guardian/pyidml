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

    def test_get_closest(self):
        spread = doc.get_children('Spread')[1]
        page_item = spread.get_children('TextFrame')[0]

        self.assertEqual(page_item.get_closest('TextFrame'), page_item)
        self.assertEqual(page_item.get_closest('Spread'), spread)
        self.assertEqual(spread.get_closest('TextFrame'), None)

    def test_get_relative_transformation_pasteboard(self):
        """
        Test get_relative_transformation() relative to the pasteboard
        """
        self.assertTrue(numpy.all(
            doc.get_relative_transformation() == 
            numpy.identity(3)
        ))
        spread = doc.get_children('Spread')[1]
        self.assertTrue(numpy.all(
            spread.get_relative_transformation() == 
            numpy.matrix([
                [1, 0, 0],
                [0, 1, 0],
                [0, 1200.472440944882, 1],
            ])
        ))
        page_item = spread.get_children('TextFrame')[0]
        self.assertTrue(numpy.all(
            page_item.get_relative_transformation() == 
            numpy.matrix([
                [1, 0, 0],
                [0, 1, 0],
                [401.10236220472433, 941.96692913385834, 1],
            ])
        ))

    def test_get_relative_transformation_relative(self):
        """
        Test get_relative_transformation() relative to other elements
        """
        page_item = doc.get_children('Spread')[1].get_children('TextFrame')[0]
        self.assertTrue(numpy.all(
            page_item.get_relative_transformation('Spread') ==
            numpy.matrix([
                [1, 0, 0],
                [0, 1, 0],
                [401.10236220472433, -258.50551181102367, 1],
            ])
        ))
        self.assertTrue(numpy.all(
            page_item.get_relative_transformation('TextFrame') == numpy.identity(3)
        ))

    def test_get_transformation(self):
        page_item = doc.get_children('Spread')[1].get_children('TextFrame')[0]
        self.assertTrue(numpy.all(
            page_item.get_transformation() ==
            numpy.matrix([
                [1, 0, 0],
                [0, 1, 0],
                [401.10236220472433, -258.50551181102367, 1],
            ])
        ))




