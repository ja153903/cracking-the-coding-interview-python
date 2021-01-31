from typing import List


def rotate(matrix: List[List[int]]):
    i, j = 0, len(matrix) - 1

    while i < j:
        matrix[i], matrix[j] = matrix[j], matrix[i]
        i += 1
        j -= 1

    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
