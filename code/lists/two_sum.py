# write a program to find all pairs of ints whose sum is equal to a given number.

# example: [2, 6, 9, 11] input: 9
# pairs that when added = 9 returns [6,3] because 6 plus 3 is 9

def twoSum(nums, target):
    # brute force:
    i = 0
    j = 0
    combo_list = []

    while i <= len(nums) - 1:
        if j < len(nums) - 1:
            j += 1
        if j == len(nums) - 1:
            if target == nums[i] + nums[j]:
                combo_list = [i, j]
            j = 0
            i += 1
        if j != i:
            sum = nums[i] + nums[j]
            if sum == target:
                combo_list = [i, j]
                return combo_list
    return combo_list
    # using cache:
    # cache = {}
    # for i in range(len(nums)):
    #     # i: 0, 1, 2, 3
    #     n = target - nums[i]
    #     # n = 24, 19, 15, 11
    #     if n not in cache:
    #         cache[nums[i]] = i
    #         print(cache)
    #     else:
    #         return [cache[n], i]


# print(twoSum([2, 7, 11, 15], 9))
# print(twoSum([2, 7, 11, 15], 18))
