# Return the reversal of an integer
def reverse(number):
    reversed_number = 0
    while number > 0:
        reversed_number = (reversed_number * 10) + number % 10
        number = number // 10
    return reversed_number


def is_palindrome(number):
    return number == reverse(number)


def main():
    number = eval(input("Enter a number: "))

    reversed_number = reverse(number)
    print('The reversed number of', number, 'is:', reversed_number)
    if number == reversed_number:
        print('It is a palindrome')
    else:
        print('It is not a palindrome')


main()
