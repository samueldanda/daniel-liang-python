import MyTriangle


def main():
    n1, n2, n3 = eval(input('Enter three sides in double: '))
    print(n1, n2, n3)
    valid = MyTriangle.is_valid(n1, n2, n3)
    print('validity', valid)
    if not valid:
        print('Input is invalid')
    else:
        print('The area of the triangle is', MyTriangle.area(n1, n2, n3))


main()
