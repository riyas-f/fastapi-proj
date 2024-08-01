

import math

def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    x1, y1 = lat1, lon1
    x2, y2 = lat2, lon2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
