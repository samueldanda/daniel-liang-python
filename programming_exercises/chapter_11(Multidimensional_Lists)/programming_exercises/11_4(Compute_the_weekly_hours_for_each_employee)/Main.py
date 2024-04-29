def main():
    n = eval(input('Enter number of employees: '))
    table = []

    for i in range(n):
        table.append([])
        work_hours = input('Enter seven days work hours (Su - Sa) for employee {}: '.format(i + 1))
        list_hours = [eval(x) for x in work_hours.split(' ')]
        table[i].extend(list_hours)

    print_table(table, n)

    print_total(table, n)


def print_total(table, n):
    total_hours = []

    for i in range(n):
        total_hours.append([])
        sum_hours = 0
        for j in range(len(table[i])):
            sum_hours += table[i][j]
        lists = [i, sum_hours]
        total_hours[i].extend(lists)

    for i in range(len(total_hours) - 1):
        for j in range(i + 1, len(total_hours)):
            if total_hours[i][1] < total_hours[j][1]:
                temp = total_hours[i]
                total_hours[i] = total_hours[j]
                total_hours[j] = temp

    print("\n{}Total".format("".ljust(13)))
    for i in range(n):
        print("Employee {}: ".format(i + 1).ljust(13), end='')
        print("{} ".format(total_hours[i][1]).rjust(6))


def print_table(table, n):
    print("{}Su M  T  W  Th F  Sa".format("".ljust(13)))
    for i in range(n):
        print("Employee {}: ".format(i + 1).ljust(13), end='')
        for j in range(len(table[i])):
            print("{}".format(table[i][j]).ljust(3), end='')
        print(end='\n')


main()
