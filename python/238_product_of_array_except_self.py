import math
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        pre = 1
        for i in range(n):
            result[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(n - 1, -1, -1):
            result[i] = result[i] * post
            post *= nums[i]

        return result


print(Solution().productExceptSelf([1, 2, 3, 4]))  # 24, 12, 8, 6
