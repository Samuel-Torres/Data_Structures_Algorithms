# What are tuples?
#   a tuple is sequence of values much like a list.
#   tuples are immutable
#   comparable & hashable. Has a value that remains the same over it's lifetime.
#


# Tuple Creation: O (1) / Space: O(n)

tup = (1, 2, 3, 4, 5)
print(tup)  # -> (1, 2, 3, 4, 5)
newTup = (1,)  # -> single element required comma else won't be tuple.
print(newTup)  # -> (1, 2, 3, 4, 5)
mytup = tuple()
print(mytup)  # ()


# Tuples in Memory:

# items stores in sequence like list. Which allows access using bracket and 0 based indices. tup[0]
# can acces using slices [:]
tup[0:3]  # -> (1, 2, 3)

# looping.
for i in tup:
    print(i)

for i in range(len(tup)):
    print("tup: ", tup[i])

# Searching: O(n)

print(1 in tup)  # -> TRUE
print(100 in tup)  # -> FALSE
# -> 0: returns index of the value being searched for in tuple.
print(tup.index(1))


def searchTup(tupl, element):
    for i in range(0, len(tupl)):
        if tupl[i] == element:
            return f"element is found at index {i}."
    return "element not found"


# print(searchTup(tup, 2))
# print(searchTup(tup, 200))
