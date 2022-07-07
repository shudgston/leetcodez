# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                print("break")
                break

            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                # search right portion; all vals to right will be smaller
                l = mid + 1
            else:
                # search left
                r = mid - 1

            print(l, r, mid)

        return res


def bs(arr, x, l, r):
    """Iterative binary searchå"""
    while l <= r:
        mid = (l + r) // 2

        if x < arr[mid]:
            r = mid - 1
        elif x > arr[mid]:
            l = mid + 1
        else:
            return mid

    return -1


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# nums = [3, 4, 5, 1, 2]
# L = 0
# R = len(nums) - 1
# print(bs(nums, 1, L, R))

# res = Solution().findMin([3, 4, 5, 1, 2])
# print(res)

res = Solution().findMin([3, 4, 5, 6, 0, 2])
print(res)
