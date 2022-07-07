# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ri = find_rotation_index(nums)
        if ri == -1:
            return binary_search(nums, target, 0, len(nums) - 1)

        if target == nums[ri]:
            return ri

        if target >= nums[ri] and target <= nums[-1]:
            half = nums[ri:]
            left = binary_search(half, target, 0, len(half) - 1)
            if left != -1:
                return ri + left
        elif target >= nums[0] and target <= nums[ri - 1]:
            half = nums[0:ri]
            right = binary_search(half, target, 0, len(half) - 1)
            if right != -1:
                return right

        return -1


def binary_search(nums, target, l, r) -> int:
    if l > r:
        return -1

    mid = (l + r) // 2

    if nums[mid] == target:
        print("found at", mid)
        return mid

    if target < nums[mid]:
        return binary_search(nums, target, l, mid - 1)
    else:
        return binary_search(nums, target, mid + 1, r)


def find_rotation_index(nums):
    for i in range(len(nums) - 1):
        if nums[i + 1] < nums[i]:
            return i + 1
    return -1


# print(Solution().search([3, 1], target=3))
# print(Solution().search([5, 1, 3], target=3))
