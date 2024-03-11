import numpy as np

my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                     12, 13, 14, 15, 16, 17, 18, 19, 20])


def find_value(array, target):
    for i in range(0, len(array)):
        if array[i] == target:
            return f"element found at index {i}"
    return "not found"


print(find_value(my_array, 12))
