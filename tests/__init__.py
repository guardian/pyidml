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
            attr = getattr(obj, k)
            self.assertEqual(
                attr,
                v,
                '%s != %s (for key %s)' % (attr, v, k)
            )
