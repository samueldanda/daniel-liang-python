import math


def is_valid(side1, side2, side3):
    if side1 + side2 > side3:
        return True
    if side2 + side3 > side1:
        return True
    if side1 + side3 > side2:
        return True
    return False


def area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
