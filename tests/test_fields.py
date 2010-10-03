# -*- coding: utf-8 -*-
from tests import FreshersTest, doc

class FieldsTest(FreshersTest):
    """
    Test the mongoengine fields in pyidml.fields work correctly
    """
    def test_parent(self):
        element = doc.get_children('Layer')[0]
        self.assertEqual(element.Properties._parent.Self, element.Self)
    
    def test_parent_through_listfield(self):
        element = doc.get_children('Layer')[0]
        self.assertEqual(element._parent, doc)
    
