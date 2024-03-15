# What is a dictionary?
# An unordered, changable, and indexed collection.
#  has key value pairs.
#  hash table
# Doesn't store each index in series.

# CREATING DICTIONARIES.
name = dict()
# print(name)
name2 = {}
# print(name2)

# Runtimes:
# Creation Time/Space Complexity when empty: O(1)
# Creation Time/Space Complexity when creating with key/vals: O(n)
# Inserting into Dictionary:


# CREATING DICTIONARY:
english_to_Spanish = dict({
    "hello": "hola",
    "why": "por que",
    "one": "uno",
})
# print(english_to_Spanish)
english_to_Spanish2 = dict(
    hello="hola",
    why="por que",
    one="uno",
)
# print(english_to_Spanish2)
english_to_Spanish3 = {
    "hello": "hola",
    "why": "por que",
    "one": "uno",
}
# print(english_to_Spanish3)
english_to_Sp = [("hello", "hola"), ("why", "por que"), ("one", "uno")]
english_to_Spanish4 = dict(english_to_Sp)

# print(english_to_Spanish4)
# -> {'one': 'uno', 'hello': 'hola', 'why': 'por que'}

sam = {"name": "Sam",  "age": 31, "birthYear": 1991}

# INSERTING DICTIONARY / UPDATING:
sam["age"] = 32  # Space/Time: O(1)
sam["weight"] = 385
# Space/Time: amortized O(1) -> some times might insert array as val / O(1)
# print(sam)

# Traversing:


# def traverse(dict):  # O(1)
#     for key in dict:  # O(n)
#         print(key, dict[key])  # O(1)


# traverse(sam)

# Searching for element in dictionary:


# def search(dict, value):  # O(1)
#     for key in dict:  # O(n)
#         if dict[key] == value:  # O(1)
#             return key, value  # O(1)
#     return "Value does not exist"  # O(1)

#  # time O(n) space O(1)


# print(search(sam, 32))
# print(search(sam, 31))

# Deleting:
# del()

# print(sam)
# del sam["age"]  # O(1) Space/Time
# print(sam)

# print(sam)
# removed = sam.pop("age", None)  # O(1) Space/Time
# removed = sam.popitem()  # O(1) Space/Time -> removes last key/val
# removed = sam.clear()  # O(1) / O(n) Space/Time -> removes all items
# print(removed)
# print(sam)

# METHODS:
# clear
# pop
# del
# copy: makes reference copy. shallow copy.

# fromkeys: fromkeys(sequence[], value) -> returns new dict with given sequence of keys as new dict
# new_sam = sam.fromkeys(["name", "age"])
# print(new_sam)

# get: (key, val) -> returns key if exists if not then returns specified value.
# print(sam.get("age", "Dan"))

# items():
# -> [('birthYear', 1991), ('age', 32), ('name', 'Sam'), ('weight', 385)]
# print(sam.items())

# keys():
# -> ['birthYear', 'age', 'name', 'weight']
# print(sam.keys())

# popitem(): returns last element
# -> ('birthYear', 1991)
# print(sam.popitem())

# setdefault(key to be searched, default value of key to be set if search key not found will set the key value pair else returns the value at the key found): returns last element

# print(sam.setdefault("name", "not found"))
# returns sam: when checking object after returns v
# ^ ->  {'birthYear': 1991, 'age': 32, 'name': 'Sam', 'weight': 385}
# print(sam.setdefault("trigger", "not found"))
# returns not found: when checking object after returns v
# ^ ->  {'birthYear': 1991, 'age': 32, 'trigger': 'not found', 'name': 'Sam', 'weight': 385}
# print(sam)


# BUILT IN FUNCTIONS:

# OPERATIONS:
# in/not in: checks if value exists in dictionary as key
# in/not in values():
# if "Sam" in sam.values():
#     print("Sam exists")

# all() checks to see if all keys are True. If False or 0 returns False.
# any() -> if all True returns True, if all False returns False, if one True returns True
# sorted(with dictionary) -> returns an array of the keys sorted.
