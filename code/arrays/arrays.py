# ARRAY MODULE - benefits more memory effecient for data types:  CONSTANT SPACE TIME O(1) if empty O(N) otherwise

# cons: supports only basic data types. Only 1 data type allowed
# from array import array
import numpy as np
import array
# i creates array/list of ints
# types:  https://drive.google.com/file/d/1ZOwjpdoTr3R04mnbYh-h_qlmnhKp5dyY/view?usp=sharing
my_array = array.array('i')
print(my_array)
my_array2 = array.array('i', [1, 2, 3, 4])
print(my_array2)

# NUMPY MODULE: CONSTANT SPACE TIME O(1) if empty O(N) otherwise

# np_array = np.array([], dtype=int)
# print(np_array)
np_array = np.array([1, 2, 3, 4])  # --> O(N) Space time complexity
print(np_array)


# ARRAY INSERTION WITH ARRAY MODULE:

# .insert(index, element to insert)

# Appending: doesn't require element shift O(1)

# Prepending: requires element shift
my_array2.insert(0, 6)  # O(N)
print("ALTERED ARRAY: ", my_array2)

# Insertion to middle: require element shift for all other elements
my_array2.insert(2, 6)  # O(N)
print("ALTERED ARRAY: ", my_array2)

# ARRAY TRAVERSAL:


def traverseArray(array):  # O(1)
    for i in array:  # O(N)
        print(i)  # O(1)


traverseArray(my_array2)

# Accessing elements of an array:
print("ACCESSED: ", my_array2[2])


def accessArray(array, index):
    if index >= len(array):
        return "There is not any element in this index"
    else:
        return array[index]


print(accessArray(my_array2, 6))
print(accessArray(my_array2, 3))


# Array Search:
def findElement(array, value):
    for i in array:
        if i <= len(array) and i == value:
            # return f"element found at index {i}"
            return i
        else:
            return "element not found"


print("SEARCH FOUND: ", findElement(my_array2, 6))
print("SEARCH FOUND: ", findElement(my_array2, 26))

# Deleting element in array:
print(my_array2)
# my_array2.remove(6)
# my_array2.remove(6) --> removes the first found value matching the parameter not the element at param index
print(my_array2)
