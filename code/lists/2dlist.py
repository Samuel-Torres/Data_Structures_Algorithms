# Given 2D list calculate the sum of diagonal elements.

# Example
# myList2D= [[1,2,3],[4,5,6],[7,8,9]]
# diagonal_sum(myList2D) # 15

def diagonal_sum(matrix):
    # create a variable named sum: this will be the sum which needs to be returned.
    sum = 0
    # create a cache: this cache:
    cache = {}
    # the key of this cache will be the current row we are in
    # the value will be whether or not we have added while in the current row.
    # if we have added we will continue to iterate.
    # create a variable called row to track which row we are in.
    # create a variable called col to track which col we are in.
    row = 0
    while row <= len(matrix) - 1:
        # check if a key/val exist in cache for the current row.
        if row not in cache:
            # if it doesn't create one and set it to true.
            cache[row] = True
            # add to the sum like so:
            # sum += the value in the matrix at matrix[row][row] in place of column.
            sum += matrix[row][row]
            row += 1
    return sum


myList2D = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

]
myList2D1 = [
    [1, 2, 3, 4],
    [4, 5, 6, 4],
    [7, 8, 9, 4],
    [7, 8, 9, 4],

]
myList2D2 = [
    [1, 2, 3, 4, 5],
    [4, 5, 6, 4, 5],
    [7, 8, 9, 5, 5]
]

print(diagonal_sum(myList2D))  # -> 15
print(diagonal_sum(myList2D1))  # -> 15
print(diagonal_sum(myList2D2))  # -> 15
