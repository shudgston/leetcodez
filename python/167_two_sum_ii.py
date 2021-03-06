from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return with_two_pointers(numbers, target)


def with_two_pointers(numbers: list, target: int):
    left = 0
    right = len(numbers) - 1

    while left < right:
        res = numbers[left] + numbers[right]

        if res == target:
            return [left + 1, right + 1]

        if res > target:
            right -= 1
        else:
            left += 1

    return []
