
integer = -1
largest = integer
total = 0
# largest_changed = False
while integer != 0:
    integer = eval(input("Enter a number (0: for end of input): "))
    if integer > largest:
        largest = integer
        total = 0

    if integer == largest:
        total = total + 1

print("The largest number is", largest)
print("The occurrence of the largest number is", total)
