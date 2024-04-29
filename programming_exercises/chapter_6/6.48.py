def format(number, width):
    number_string = str(number)

    while len(number_string) < width:
        number_string = '0' + number_string

    return number_string


def main():
    integer = eval(input('Enter an integer: '))
    width = eval(input('Enter the width: '))
    print('The formatted number is: ' + format(integer, width))


main()
