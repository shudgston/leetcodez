# https://leetcode.com/problems/search-a-2d-matrix/
"""
Problem statement:

    Write an efficient algorithm that searches for a value target in an m x n
    integer matrix matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

1. Find the row that the target could be in. Binary search the rows by comparing the
   target against the values in the first column and last column.
2. If such a row is found, binary search the row itself.

Time Complexity:
O(log(m*n))  standard binary search time

Space:
O(1) constant
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return bin_search_matrix(matrix, target)


def bin_search_matrix(matrix: List[List[int]], target: int):
    if target < matrix[0][0] or target > matrix[-1][-1]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    if rows == 1:
        return bin_search_row(matrix[0], target, 0, cols)

    row_i = find_row(matrix, target, 0, rows)

    if row_i == -1:
        return False

    return bin_search_row(matrix[row_i], target, 0, cols)


def find_row(matrix, x, left, right):
    """Find the row that the target could be in"""
    if left > right:
        return -1

    mid = (left + right) // 2

    if x >= matrix[mid][0] and x <= matrix[mid][-1]:
        # its in this row
        return mid

    if x < matrix[mid][0]:
        return find_row(matrix, x, left, mid - 1)
    elif x > matrix[mid][-1]:
        return find_row(matrix, x, mid + 1, right)


def bin_search_row(row: list, x: int, left: int, right: int):
    if left > right:
        return False

    if len(row) <= 2:
        return x in row

    mid = (left + right) // 2

    if x == row[mid]:
        return True

    if x < row[mid]:
        return bin_search_row(row, x, left, mid - 1)
    elif x > row[mid]:
        return bin_search_row(row, x, mid + 1, right)


print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 8))
print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(Solution().searchMatrix([[1], [3], [5]], 5))
print(Solution().searchMatrix([[1], [3]], 4))
print(Solution().searchMatrix([[1], [3], [5]], 5))
print(Solution().searchMatrix([[1, 2, 3, 4, 7, 10]], 11))
