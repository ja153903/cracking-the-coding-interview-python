from typing import List, Set


def zero_matrix(matrix: List[List[int]]):
    zero_row: Set[int] = set()
    zero_col: Set[int] = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                zero_row.add(i)
                zero_col.add(j)

    for row in zero_row:
        for i in range(len(matrix[row])):
            matrix[row][i] = 0

    for col in zero_col:
        for i in range(len(matrix)):
            matrix[i][col] = 0
