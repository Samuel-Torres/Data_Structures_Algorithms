def max_value_key(my_dict):
    highest_key = ''
    highest_val = 0
    for key in my_dict:
        if my_dict[key] > highest_val:
            highest_val = my_dict[key]
            highest_key = key
        else:
            continue
    return highest_key


my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key(my_dict))
