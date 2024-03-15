def frequency(words):
    count = {}
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    return count


words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
print(frequency(words))

# Time: O(n)
# Space: O(n)
