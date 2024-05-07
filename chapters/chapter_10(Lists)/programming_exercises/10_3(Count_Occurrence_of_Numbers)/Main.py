def main():
    s = input("Enter integers between 1 and 100: ")
    num_list = s.split()
    num_unique_list = []
    num_count_list = []

    for num in num_list:
        if num not in num_unique_list:
            num_unique_list.append(num)
            num_count_list.append(0)

        num_count_list[num_unique_list.index(num)] = num_count_list[num_unique_list.index(num)] + 1

    num_unique_list = [eval(x) for x in num_unique_list]

    sort_list(num_unique_list, num_count_list)

    for i in range(len(num_unique_list)):
        print("{} occurs {} {}".format(num_unique_list[i], num_count_list[i],
                                       "times" if num_count_list[i] > 1 else "time"))


def sort_list(num_unique_list, num_count_list):
    print(num_unique_list, end=" ")
    print(num_count_list)
    for i in range(len(num_unique_list) - 1):
        for j in range(i + 1, len(num_unique_list)):
            if num_unique_list[i] > num_unique_list[j]:
                temp = num_unique_list[i]
                num_unique_list[i] = num_unique_list[j]
                num_unique_list[j] = temp

                temp = num_count_list[i]
                num_count_list[i] = num_count_list[j]
                num_count_list[j] = temp


main()
