import math
from tsp.tsp_file import TSPFileFormat


class Coordinate:
    def compute_distance(self, c):
        pass


class SimplePoint(Coordinate):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compute_distance(self, c):
        return math.sqrt((self.y - c.y) ** 2 + (self.x - c.x) ** 2)

    def __str__(self) -> str:
        return (self.x, self.y)


class Radian(Coordinate):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def compute_distance(self, c):
        RRR = 6378.388

        q1 = math.cos(self.longitude - c.longitude)
        q2 = math.cos(self.latitude - c.latitude)
        q3 = math.cos(self.latitude + c.latitude)

        return math.trunc(
            RRR * math.acos(0.5 * ((1.0 + q1) * q2 - (1.0 - q1) * q3)) + 1.0
        )

    def __str__(self) -> str:
        return (self.latitude, self.longitude)


file_type_to_point = {
    TSPFileFormat.GEO.value: Radian,
    TSPFileFormat.EUC_2D.value: SimplePoint,
}


def create_point(x, y, format: TSPFileFormat):
    Point = file_type_to_point[format]

    return Point(x, y)
