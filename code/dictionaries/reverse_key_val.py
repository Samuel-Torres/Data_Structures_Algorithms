def reverse_dict(my_dict):
    return {val: key for (key, val) in my_dict.items()}


my_dict = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(my_dict))
# should output: {1: 'a', 2: 'b', 3: 'c'}
