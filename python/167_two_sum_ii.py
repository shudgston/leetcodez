from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}  # value: index

        for i in range(len(numbers)):
            diff = target - numbers[i]

            if diff in seen:
                return [seen[diff] + 1, i + 1]

            seen[numbers[i]] = i

        return []
