START_NUMBER = 1
END_NUMBER = 10000

total = 0
for i in range(START_NUMBER, END_NUMBER):
    for j in range(1, i - 1):
        if i % j == 0:
            total += j
    if total == i:
        print(i)
    total = 0
