# https://leetcode.com/problems/valid-sudoku/

from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_size = 9

        rows = [set() for _ in range(board_size)]
        cols = [set() for _ in range(board_size)]

        boxes = defaultdict(set)  # tuple: list

        for r in range(board_size):
            for c in range(board_size):
                if board[r][c] == ".":
                    continue

                digit = int(board[r][c])

                if digit in rows[r]:
                    return False
                else:
                    rows[r].add(digit)

                if digit in cols[c]:
                    return False
                else:
                    cols[c].add(digit)

                box = current_box(r, c)
                if digit in boxes[box]:
                    return False
                else:
                    boxes[box].add(digit)

        return True


def current_box(row: int, col: int, boxsize: int = 3) -> tuple:
    return row // boxsize, col // boxsize


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


print(Solution().isValidSudoku(board))
