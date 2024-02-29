# When to use/avoid array:

# Use when:
# • You want to store multiple variables of the same data type.
# • Random access: accessing data takes constant runtime O(1).
# •

# When to avoid:
# • Storing different data types that are not the same.
# • Need to reserve memory. Duplicates mem storage.

# Daily Temperatures:

# Day 1 = 11, 15, 10, 6
# Day 2 = 10, 14, 11, 5
# Day 3 = 12, 17, 12, 8
# Day 4 = 15, 18, 14, 9

import numpy as np


twoDArray = np.array([[11, 15, 10, 6],
                      [10, 14, 11, 5],
                      [12, 17, 12, 8],
                      [15, 18, 14, 9]
                      ])  # O(m, n)

print(twoDArray)

# Insertion:
# can't have uneven matrix.
# can add column or row.


# Adding column: O(mn)
# [3]
# [6]
# [9]
# [7]

newTwoDArray = np.insert(twoDArray, 0, [3, 6, 9, 7], axis=1)
print(newTwoDArray)

# Adding row: O(mn)
# [3, 6, 9, 7]

newTwoDArray2 = np.insert(twoDArray, 0, [3, 6, 9, 7], axis=0)
print(newTwoDArray2)

# appending row: O(mn)
newTwoDArray2 = np.append(twoDArray, [[9, 4, 2, 1]], axis=0)
print(newTwoDArray2)

# appending column: O(mn)
newTwoDArray2 = np.append(twoDArray, [[9], [4], [2], [1]], axis=1)
print(newTwoDArray2)

# Accessing 2d array:
# directly
print(newTwoDArray2[0][3])
# with function:


def getElement(array, rowIndex, colIndex):  # O(1)
    if rowIndex >= len(array) or colIndex >= len(array[0]):  # O(1)
        return "You're seeking an element out of range"
    return array[rowIndex][colIndex]  # O(1)


print("result: ", getElement(newTwoDArray2, 3, 4))  # O(1)

# Traverse 2D array:

# for arr in newTwoDArray2:
#     for i in arr:
#         print("ELEMENT: ", i)


def traverseArray(array):
    for arr in newTwoDArray2:  # O(mn)
        for i in arr:  # O(n)
            print(i)  # O(1)
# O(mn)
    # for i in range(len(array)):
    #     for j in range(len(array[0])):
    #         print(array[i][j])


print(traverseArray(newTwoDArray))


# Searching for element in 2D array:
def findElement(array, elementToFind):  # O(mn)
    for arr in array:  # O(mn)
        for i in arr:  # O(n)
            if i == elementToFind:
                return i
    return "element is not in array"


print(findElement(newTwoDArray2, 122))

#  Deletion of element in 2D array: O(mn)
# delete column:
print(newTwoDArray2)
newArr = np.delete(newTwoDArray2, 0, axis=1)
#  delete row:
newArr2 = np.delete(newArr, 0, axis=0)

print(newArr)
print(newArr2)
