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
    number = eval(input("Enter limit number: "))

    for i in range(10, number + 1):
        reversed_number = reverse(i)
        if i == reversed_number:
            print(i)


main()
