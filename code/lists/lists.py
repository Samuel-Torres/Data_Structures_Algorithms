import random
import numpy as np
# Similarities & Difference between List & Arrays:

# Sim:
# 1. Mutable
# 2. Both can be indexed & iterated through
# 3. Can be sliced

# Diffs:
# 1. Arithmetic Operations are different better to use array for arithmetic operations
arr = np.array([1, 2, 3])
list2 = [1, 2, 3]

print("RESULT: ", arr / 2)  # works --> ('RESULT: ', array([0, 1, 1]))
# print("RESULT: ", list2 / 2)  # breaks doesn't work --> error
# 2. All element types in array have to remain the same type in lists can take any data type per element


# Lists:
# Lists is a built in data structure that stores and ordered collection of items(not type specific like arrays).
# Lists can have nested lists.
# Lists are mutable data structure.

# declaring a list:

# variableName = [item, item, item]:
numbersList = [1, 2, 3, 4]
print(numbersList)

# List Traversal:
# for each in numbersList:
#     print(each)

# Accessing List:
# print(numbersList[2])

# in operator:
# example: 2 in numbersList
print(2 in numbersList)  # --> returns True
print(387238 in numbersList)  # --> returns False

# Get last element:
print(numbersList[-1])  # --> gets last element.
# -2 and below works backwards on the list --> gets last element.
print(numbersList[-2])  # --> 3

# for i in range(len(numbersList)): --> gives you number range of indices to traverse with
for i in range(len(numbersList)):
    print("before: ", numbersList[i])
    numbersList[i] = numbersList[i] + 1
    print("after: ", numbersList[i])
print(numbersList)

# Update/Insert list:
# -> Updates indexes 0, 1, 2, 3 stops at 4 with the array elements
numbersList[0:4] = [1, 2, 3, 4]
print(numbersList)

numbersList[0] = 0  # --> O(1) space complexity also O(1)
print(numbersList)
numbersList[0] = 1
print(numbersList)

# Insertion: insert, append, extend

# insert:
# --> O(n) because all other elements have to shift right 1 index unless last index
numbersList.insert(0, 0)  # ---> time: O(n) space: O(1)
print(numbersList)
numbersList.append(5)  # --> time: O(1) space: O(1)
print(numbersList)
numbersList.extend([6, 7, 8])  # --> O(n) space: --> O(n)
print(numbersList)


# Slice/Deleting:
# slice:
print(numbersList[0:2])  # returns [0, 1] <<< slice
print(numbersList[0:])  # returns [all elements]
print(numbersList[:])  # returns [all elements]
print(numbersList[:3])  # returns [0, 1, 2]
# delete: pop, delete, remove
numbersList.pop()  # removes 8 last element or element at specified index O(1)
print(numbersList)
# removes 1 --> elements have to shift after pop so O(n) returns deleted element
print(numbersList.pop(1))  # returns 1
print(numbersList)
# --> removes defined element value not index: numbers shift O(n)
numbersList.remove(2)
print(numbersList)

del numbersList[0]  # deletes first element all numbers shift O(n)
print(numbersList)
del numbersList[0:2]  # can delete range
print(numbersList)


# Searching:

# in operator:
# if 4 in numbersList: # --> No
if 5 in numbersList:  # --> Yes O(n)
    print("Yes")
else:
    print("no")
# in has better runtime in sets & dictionary

# linear search.


def searchForNum(numList, target):  # --> O(n)
    # for num in numList:
    #     if num == target:
    #         return "Found"
    #     else:
    #         return "Not Found"

    for i, value in enumerate(numList):
        if value == target:
            return ("Found at index: ", i)
    return "Not Found"


print(searchForNum(numbersList, 4))  # --> Not Found
print(searchForNum(numbersList, 5))  # --> ("Found at index: ", 0)

# List operations:


# + operator: concatonates lists together.
list_one = ["a", "b", "c"]
list_two = [1, 2, 3]
newer_list = list_one + list_two
print(newer_list)

# * operator: multiplies the elements x number of times in series within new array.
newer_list2 = newer_list * 3
# --> ['a', 'b', 'c', 1, 2, 3, 'a', 'b', 'c', 1, 2, 3, 'a', 'b', 'c', 1, 2, 3]
print(newer_list2)

# len
print(len(newer_list2))  # --> Returns the number of items in a container.
# max returns the largest item in the list
print(max(list_two))  # --> 3
# max returns the smallest item in the list
print(min(list_two))  # --> 1
# sum: combines the value of all elements within the list.
print(sum(list_two))  # --> 6


# List & Strings:

# converting word into list of strings by individual character:
my_string = "Samuel Torres"
name_to_string = list(my_string)
# --> ['S', 'a', 'm', 'u', 'e', 'l', ' ', 'T', 'o', 'r', 'r', 'e', 's']
print(name_to_string)

my_string_name = "Samuel Rilla Torres"
my_string_name2 = "Samuel-Rilla-Torres"
name_to_string2 = my_string_name.split()
name_to_string3 = my_string_name2.split("-")
print(name_to_string2)  # --> ['Samuel', 'Rilla', 'Torres']
print(name_to_string3)  # --> ['Samuel', 'Rilla', 'Torres']

# join: list to string
my_new_string = " "
print(my_new_string.join(name_to_string3))


# Common pitfalls and how to avoid them:
# docs.python.com


prev_list = [1, -2, 3]
# List Comprehension:
another_list = [item * 2 for item in prev_list]
print(another_list)

# Conditional list Comprehension:
cond_list = [item * 2 for item in prev_list if item >= 0]
cond_list2 = [item * 2 if item >= 0 else item for item in prev_list]
print("FIRST: ", cond_list)
print("SECOND: ", cond_list2)


sentence = "I am a sentence"


def is_consonant(letter):
    vowels = "aeiou"
    return letter.isalpha() and letter.lower() not in vowels


consonants = [i for i in sentence if is_consonant(i)]
print(consonants)
random.shuffle(consonants)
print(consonants)


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a[:2] = 10, 20, 30, 40, 50, 60
# this code slices out indexes 0, 1, 2 and inputs the values 10 - 60 in its
# places and shifts all other values after it.
# print(a)

# this code below prints every 2nd element in the array if 3 would print every 3rd element
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[::2])
