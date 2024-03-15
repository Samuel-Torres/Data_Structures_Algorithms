def filter_dict(my_dict, condition):
    return {key: val for (key, val) in my_dict.items() if condition(key, val)}


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(filter_dict(my_dict, lambda k, v: v % 2 == 0))
# expected output: {'b': 2, 'd': 4}
