import unittest
from unittest.mock import MagicMock

from cfb_stats.parse.parsers import SplitIntParser

class TestSplitIntParser(unittest.TestCase):
    def test_split_int_short(self):
        data = '0 - 12 - 273'
        o = MagicMock()
        p = SplitIntParser(['k', 'e'], o, [1,2])
        p.parse(data)
        self.assertEqual(o.k, 12)
        self.assertEqual(o.e, 273)

    def test_split_int_reverse(self):
        data = '12 - 273'
        o = MagicMock()
        p = SplitIntParser(['k', 'e'], o, [1,0])
        p.parse(data)
        self.assertEqual(o.k, 273)
        self.assertEqual(o.e, 12)

    def test_split_int_middle(self):
        data = '12 - 273 - 0'
        o = MagicMock()
        p = SplitIntParser(['k'], o, [1])
        p.parse(data)
        self.assertEqual(o.k, 273)

    def test_split_int_only(self):
        data = '12'
        o = MagicMock()
        p = SplitIntParser(['e'], o)
        p.parse(data)
        self.assertEqual(o.e, 12)
