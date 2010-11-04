import os
import pyidml
import unittest

doc = pyidml.parse(os.path.join(
    os.path.dirname(__file__),
    'samples/freshers.idml'
))

class FreshersTest(unittest.TestCase):
    def assertProps(self, obj, **kwargs):
        for k, v in kwargs.items():
            attr = obj
            for prop in k.split('__'):
                attr = getattr(attr, prop, None)
            self.assertEqual(
                attr,
                v,
                '%s != %s (for key %s)' % (attr, v, k)
            )
    
    def assertElement(self, element, name, **kwargs):
        self.assertEqual(element.__class__.__name__, name)
        self.assertProps(element, **kwargs)
    
