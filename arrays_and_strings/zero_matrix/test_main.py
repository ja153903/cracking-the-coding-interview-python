import pytest
from typing import List
from .main import zero_matrix

IntMatrix = List[List[int]]


@pytest.mark.parametrize("matrix,expected", [
    ([[0, 1, 1], [1, 1, 1], [1, 1, 1]], [[0, 0, 0], [0, 1, 1], [0, 1, 1]])
])
def test_zero_matrix(matrix: IntMatrix, expected: IntMatrix):
    zero_matrix(matrix)

    assert matrix == expected
