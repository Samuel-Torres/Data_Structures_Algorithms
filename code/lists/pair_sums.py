# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

def pair_sum(myList, sum):
    # create cache:
    # create a return list
    # assign i and j to 0
    # enter quadratic loop in a while loop
    # check if i & j are the same number if it is then j += 1
    # cache key/val is going to be the indices of the pair which adds up to the sum
    # check if the key/val is in the cache index.
    # if it isn't then add it to the cache.
    # append the values that add up to sum to the return list.
    # and then store the value of the numbers in those indices as the 2 numbers which add up to the sum.
    # if the number is in the cache then continue
    my_cache = {}
    return_list = []
    i, j = 0, 0
    while i <= len(myList) - 1:
        if i == j and j < len(myList) - 1:
            j += 1
        if (i, j) not in my_cache:
            if (j, i) not in my_cache and myList[i] + myList[j] == sum:
                my_cache[(i, j)] = True
                return_list.append(f'{myList[i]}+{myList[j]}')
        if j < len(myList):
            j += 1
        if j >= len(myList):
            j = 0
            i += 1

    return return_list


# Example:
print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))
# print(pair_sum([3, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))
Output: ['2+5', '4+3', '3+4', '-2+9']


# Note:
# 4+3 comes from second and third elements from the main list.
# 3+4 comes from third and seventh elements from the main list.
