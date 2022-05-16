import unittest

from tsp.points import SimplePoint, RadianPoint


class SimplePointTest(unittest.TestCase):
    def test_distance_from_origin(self):
        O = SimplePoint(0, 0)
        p = SimplePoint(5, 5)

        actual = p.compute_distance(O)
        expected = 7

        self.assertEqual(expected, actual)

    def test_distance_between_two_points(self):
        O = SimplePoint(-10, -20)
        p = SimplePoint(60, 54)

        actual = p.compute_distance(O)
        expected = 102

        self.assertEqual(expected, actual)


class RadianTest(unittest.TestCase):
    def test_radian_conversion(self):
        actual = RadianPoint(16.47, 96.10)
        expected = {"latitude": 0.29292436518518516, "longitude": 1.6784246148148148}

        self.assertEqual(actual.latitude, expected["latitude"])
        self.assertEqual(actual.longitude, expected["longitude"])

    def test_distance_from_origin(self):
        O = RadianPoint(0, 0)
        p = RadianPoint(16.47, 96.10)

        actual = p.compute_distance(O)
        expected = 10677

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
