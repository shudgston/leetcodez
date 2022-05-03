# https://leetcode.com/problems/binary-search/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bin_search(nums, target, 0, len(nums) - 1)


def bin_search(nums: list, target: int, left: int, right: int):
    if right < left:
        return -1

    mid = right - left // 2

    if target == nums[mid]:
        return mid

    if target < nums[mid]:
        # slide to the left
        return bin_search(nums, target, left, mid - 1)
    else:
        # slide to the right
        return bin_search(nums, target, mid + 1, right)
    # criss cross criss cross
    # cha cha real smooth
