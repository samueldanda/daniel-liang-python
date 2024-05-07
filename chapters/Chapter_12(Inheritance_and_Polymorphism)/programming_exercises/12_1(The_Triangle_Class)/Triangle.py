import math
from GeometricObject import GeometricObject


class Triangle(GeometricObject):
    __side1: float
    __side2: float
    __side3: float

    def __init__(self, color="green", filled=True, side1=1.0, side2=1.0, side3=1.0):
        super().__init__(color, filled)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def get_side1(self):
        return self.__side1

    def set_side1(self, side1):
        self.__side1 = side1

    def get_side2(self):
        return self.__side2

    def set_side2(self, side2):
        self.__side2 = side2

    def get_side3(self):
        return self.__side3

    def set_side3(self, side3):
        self.__side3 = side3

    def get_area(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        return math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))

    def get_perimeter(self):
        return self.get_side1() + self.get_side2() + self.get_side3()

    def __str__(self):
        return "Triangle: side1 = " + str(self.get_side1()) + " side2 = " + str(self.get_side2()) + " side3 = " + str(
            self.get_side3())
