import unittest

from .geotools import distance, get_lat_lon


class TestGeoTool(unittest.TestCase):
    def test_get_lat_lon(self):
        self.assertEqual(get_lat_lon("Paris"), "48.85341,2.3488")  # add assertion here

    def test_distance(self):
        lls = ['50.9787,11.03283', '51.01454,11.04377']
        self.assertEqual(4.058106290330106, distance(lls))

    def test_distance2(self):
        lls = ['50.9787,11.03283', '52.52437,13.41053', '51.01454,11.04377']
        self.assertEqual(4.058106290330106, distance(lls))


if __name__ == '__main__':
    unittest.main()
