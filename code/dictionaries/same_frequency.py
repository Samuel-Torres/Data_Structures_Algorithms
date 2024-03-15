def check_same_frequency(list1, list2):
    list_one = {num: list1.count(num) for num in list1}
    list_two = {num: list2.count(num) for num in list2}

    return list_one == list_two


list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))
