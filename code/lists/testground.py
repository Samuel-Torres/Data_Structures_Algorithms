def heightChecker(heights):
    expected = sorted(heights)  # uses Tim sort algo O(n)
    curr_ind = 0
    count = 0
    expectedHeights = {}

    for height in expected:
        expectedHeights[curr_ind] = height
        curr_ind += 1
    curr_ind = 0

    for height in heights:
        if expectedHeights[curr_ind] != height:
            count += 1
        curr_ind += 1
    return count

# time: O(mn)
# space: O(n)


# print(heightChecker([1, 1, 4, 2, 1, 3]))


def heightCheckerOptimal(heights):
    count = 0
    sortedHeights = sorted(heights)

    def zipToTuples(list1, list2):
        cur_ind = 0
        shortest_list = None
        new_arr = []

        if(len(list1) < len(list2)):
            shortest_list = list1
        else:
            shortest_list = list2

        while cur_ind <= len(shortest_list) - 1:
            new_arr.append((list1[cur_ind], list2[cur_ind]))
            cur_ind += 1

        return new_arr

    zipped = zipToTuples(sortedHeights, heights)

    for i in zipped:
        if i[0] != i[1]:
            count += 1
    return count


print(heightCheckerOptimal([1, 1, 4, 2, 1, 3]))
