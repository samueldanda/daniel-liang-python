from Triangle import Triangle


def main():
    side1, side2, side3 = eval(input('Enter the three sides of triangle: '))
    color = input('Enter the color of the triangle: ')
    filled = input('Enter 0 or 1 if the triangle is filled: ')

    triangle = Triangle(color, True if filled == "1" else False, float(side1), float(side2), float(side3))

    print("\nA Triangle color: {} and filled: {}".format("True" if triangle.get_color() else "False",
                                                         triangle.get_filled()))
    print("The side 1 is: {}".format(side1))
    print("The side 2 is: {}".format(side2))
    print("The side 3 is: {}".format(side3))


main()
