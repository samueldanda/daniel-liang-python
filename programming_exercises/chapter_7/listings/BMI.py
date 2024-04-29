class BMI:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    def get_bmi(self):
        weight_in_pounds = self.__weight
        kilograms_per_pound = 0.45359237
        weight_in_kilograms = weight_in_pounds * kilograms_per_pound

        height_in_inches = self.__height
        meters_per_inches = 0.0254
        height_in_meters = height_in_inches * meters_per_inches

        return weight_in_kilograms / (height_in_meters * height_in_meters)
        # bmi = round(bmi, 4)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_weight(self):
        return self.__weight

    def get_height(self):
        return self.__height
