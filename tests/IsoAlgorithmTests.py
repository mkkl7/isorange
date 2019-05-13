import unittest
import zones_calculator


class TestIso(unittest.TestCase):
    def setUp(self):
        self.zc = zones_calculator.zc()


class TestLoad(TestIso):
    def test_load(self):
        self.zc.loadfromshp('mock\mock_links.shp')
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
