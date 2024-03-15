def rotate(matrix):
    length = len(matrix)

    for i in range(length):
        for j in range(i, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for eachRow in matrix:
        eachRow.reverse()

    return matrix


print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
