# # myList = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# # for i in range(0, len(myList)):
# #     if i == 1:
# #         del(myList[i])
# #         myList.append(None)
# #     else:
# #         continue

# # print(myList)
# def removeDuplicates(nums):
#     # assign count to a variable at 0
#     count = 0
#     # assign curr_index to 0
#     next_index = 0
#     curr_index = 0

#     # enter while loop cond while current index is less than or equal to len of nums minus 1
#     while curr_index <= len(nums) - 1:
#         # assign next index to current index plus 1 as long as the item in the next position isn't None.
#         if curr_index + 1 <= len(nums) - 1:
#             next_index = curr_index + 1
#             # if the next item is None then assign the current index to len of nums + 1 ending while loop.
#         elif next_index >= len(nums) - 1:
#             count += 1
#             # print("SECOND: ", count)
#             break
#         # print(curr_index, next_index)
#         # check to see if next element in nums at next index is equal to the current index
#         if next_index <= len(nums) - 1 and nums[next_index] == nums[curr_index]:
#             # if it is then delete current index and append None to the nums array.
#             del(nums[curr_index])
#             # nums.append(None)
#             # before leaving that cond check again if current index and next are the same.
#             if next_index <= len(nums) - 1 and nums[next_index] == nums[curr_index]:
#                 # if it is then remove current index again and append None.
#                 del(nums[curr_index])
#                 # nums.append(None)
#             # iterate again
#         count += 1
#         # print("FIRST: ", count)
#         curr_index += 1
#     return (count, nums)


# print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
# print(removeDuplicates([1, 1, 2]))
# print(removeDuplicates([1, 2]))
# print(removeDuplicates([1, 1]))
# print(removeDuplicates([1, 2]))


def getConcatenation(nums):
    newList = [num for num in nums * 2]
    return newList


print(getConcatenation([1, 2, 1]))
print(getConcatenation([1, 3, 2, 1]))
