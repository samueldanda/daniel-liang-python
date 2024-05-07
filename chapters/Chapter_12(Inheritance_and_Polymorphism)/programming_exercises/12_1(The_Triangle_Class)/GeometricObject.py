class GeometricObject:
    __color: str
    __filled: bool

    def __init__(self, color="green", filled=True):
        self.__color = color
        self.__filled = filled

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_filled(self):
        return self.__filled

    def set_filled(self, filled):
        self.__filled = filled

    def __str__(self):
        return "color: " + self.get_color() + " filled: " + str(self.get_filled())
