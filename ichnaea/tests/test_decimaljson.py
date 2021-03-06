from decimal import Decimal
from unittest import TestCase
from datetime import date
from datetime import datetime
from datetime import timedelta

from ichnaea.decimaljson import dumps


class TestRenderer(TestCase):

    def _make_one(self):
        from ichnaea.decimaljson import Renderer
        return Renderer()(None)

    def test_basic(self):
        render = self._make_one()
        self.assertEqual(render({'a': 1}, {}), '{"a": 1}')

    def test_date(self):
        render = self._make_one()
        self.assertEqual(render({'d': date(2012, 5, 17)}, {}),
                         '{"d": "2012-05-17"}')

    def test_datetime(self):
        render = self._make_one()
        self.assertEqual(render({'d': datetime(2012, 5, 17, 14, 28, 56)}, {}),
                         '{"d": "2012-05-17T14:28:56.000000"}')

    def test_decimal(self):
        render = self._make_one()
        d = Decimal("12.345678")
        self.assertEqual(render({'a': d}, {}), '{"a": 12.345678}')

    def test_decimal_low_precision(self):
        render = self._make_one()
        d = Decimal("12.34")
        self.assertEqual(render({'a': d}, {}), '{"a": 12.34}')

    def test_error(self):
        self.assertRaises(TypeError, dumps, timedelta(days=1))
