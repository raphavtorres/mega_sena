list = [1, 1, 2, 5, 5, 6]


def count_number_occurrences(list):
    count_list = []
    count = 1
    for i in range(len(list) - 1):
        a = list[i]
        b = list[i+1]
        if a != b:
            count_list.append(count)
            count = 0
            while (a+1) != b:
                count_list.append(count)
                a += 1
        count += 1
    count_list.append(count)
    return count_list


print(count_number_occurrences(list))
