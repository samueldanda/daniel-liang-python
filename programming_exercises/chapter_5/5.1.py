# Prompt for integers until input is 0
total = 0
number_of_positives = 0
number_of_negatives = 0

integer = -1
while integer != 0:
    integer = eval(input("Enter an integer, the input ends if it is 0: "))

    if integer < 0:
        number_of_negatives += 1
    elif integer > 0:
        number_of_positives += 1

    total += integer

average = total / (number_of_positives + number_of_negatives)

print("The number of positives is ", number_of_positives)
print("The number of negatives is ", number_of_negatives)
print("The total is ", total)
print("The average is ", average)
