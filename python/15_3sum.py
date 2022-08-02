import enum
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)  # nlogn
        res = []

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                t = val + nums[l] + nums[r]

                if t > 0:
                    r -= 1
                elif t < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # update left point, skipping duplicate values
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res


tests = [
    [-3, 3, 4, -3, 1, 2],
    [-1, 0, 1, 2, -1, -4],
    [0, 0, 0, 0],
]

for t in tests:
    out = Solution().threeSum(t)
    print(out)
