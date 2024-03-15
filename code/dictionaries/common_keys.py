def merge_dicts(dict1, dict2):
    new_dict = {letter: num for (letter, num) in dict1.items()}

    for key, val in dict2.items():
        if key not in new_dict:
            new_dict[key] = val
        else:
            new_dict[key] = new_dict[key] + val
    return new_dict


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}


print(merge_dicts(dict1, dict2))
# should return:{'a': 1, 'b': 5, 'c': 7, 'd': 5}

# time: O(nm)
# space: O(n)
