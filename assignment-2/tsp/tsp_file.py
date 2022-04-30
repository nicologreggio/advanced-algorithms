from enum import Enum


class TSPLabel(Enum):
    NAME = "NAME"
    TYPE = "TYPE"
    COMMENT = "COMMENT"
    DIMENSION = "DIMENSION"
    EDGE_WEIGHT_TYPE = "EDGE_WEIGHT_TYPE"
    EDGE_WEIGHT_FORMAT = "EDGE_WEIGHT_FORMAT"
    DISPLAY_DATA_TYPE = "DISPLAY_DATA_TYPE"
    NODE_COORD_SECTION = "NODE_COORD_SECTION"
    OPTIMAL_SOLUTION = "OPTIMAL_SOLUTION"
    EOF = "EOF"

    def __str__(self):
        return self.value


class TSPFileFormat(Enum):
    GEO = "GEO"
    EUC_2D = "EUC_2D"

    def __str__(self):
        return self.value
