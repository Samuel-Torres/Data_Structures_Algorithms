from array import *

# 1. Create an array and traverse.
my_array = array("i", [1, 2, 3, 4])

# 2. Access individual elements through indexes
for i in my_array:
    print(i)

# 3. Append any value to the array using append() method
my_array.append(5)
print(my_array)

# 4. Insert value in an array using insert() method
my_array.insert(1, 3)
my_array.insert(1, 3)
print(my_array)

# 5. Extend python array using extend() method
my_array.extend([6, 7, 8])
print(my_array)

# 6. Add items from list into array using fromlist() method
new_list = [9, 10]
my_array.fromlist(new_list)
print(my_array)

# 7. Remove any array element using remove() method
my_array.remove(3)
print(my_array)

# 8. Remove last array element using pop() method
my_array.pop()
print(my_array)

# 9. Fetch any element through its index using index() method
fetched_element = my_array.index(8)
# --> return index value of 8 in array not the 8th index
print(fetched_element)

# 10. Reverse a python array using reverse() method
my_array.reverse()
print(my_array)

# 11. Get array buffer information through buffer_info() method
my_array.buffer_info()
print("BUFFER: ", my_array)

# 12. Check for number of occurrences of an element using count() method
count = my_array.count(3)
print("3 Appears this many times: ", count)

# 14. Convert array to a python list with same elements using tolist() method
myList = my_array.tolist()
print(myList)

# 15. Append a string to char array using fromstring() method
# myList.append()

# 16. Slice Elements from an array
print(my_array[0:3])
