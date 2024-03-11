# Write a function to remove the duplicate numbers on given integer array/list.

def remove_duplicates(arr):
    cache = {}
    new_arr = []
    for i in arr:
        if i not in cache:
            cache[i] = True
            new_arr.append(i)
        else:
            continue
    return new_arr


# start 11:35
print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))
# Output : [1, 2, 3, 4, 5]
