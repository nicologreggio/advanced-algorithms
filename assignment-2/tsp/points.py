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
        return round(math.sqrt((self.y - c.y) ** 2 + (self.x - c.x) ** 2))

    def __str__(self) -> str:
        return (self.x, self.y)


class Radian(Coordinate):
    def __init__(self, x, y):
        def to_radian(d):
            PI = 3.141592

            integer_part = int(d)
            decimal_part = d - integer_part
            rad = PI * (integer_part + 5.0 * decimal_part / 3.0) / 180.0

            return rad

        self.latitude = to_radian(x)
        self.longitude = to_radian(y)

    def compute_distance(self, c):
        RRR = 6378.388

        q1 = math.cos(self.longitude - c.longitude)
        q2 = math.cos(self.latitude - c.latitude)
        q3 = math.cos(self.latitude + c.latitude)

        return int(RRR * math.acos(0.5 * ((1.0 + q1) * q2 - (1.0 - q1) * q3)) + 1.0)

    def __str__(self) -> str:
        return (self.latitude, self.longitude)


filetype_to_point = {
    TSPFileFormat.GEO.value: Radian,
    TSPFileFormat.EUC_2D.value: SimplePoint,
}


def init_point(x, y, format: TSPFileFormat) -> Coordinate:
    Point = filetype_to_point[format]

    return Point(x, y)
