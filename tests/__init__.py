import os
import pyidml
import unittest

class FreshersTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        """
        In __init__ for speed - if doc is modified, move this to setUp()
        """
        super(FreshersTest, self).__init__(*args, **kwargs)
        self.doc = pyidml.parse(os.path.join(
            os.path.dirname(__file__),
            'samples/freshers.idml'
        ))
    
    def assertProps(self, obj, **kwargs):
        for k, v in kwargs.items():
            attr = getattr(obj, k)
            self.assertEqual(
                attr,
                v,
                '%s != %s (for key %s)' % (attr, v, k)
            )
