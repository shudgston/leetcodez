from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # return bruteforce(height)
        return twopointer(height)


def bruteforce(height):
    # brute force
    n = len(height)
    maxarea = 0

    for a in range(0, n - 1):
        for b in range(a + 1, n):
            area = min(height[a], height[b]) * (b - a)
            maxarea = max(maxarea, area)

    return maxarea


def twopointer(height):
    left = 0
    right = len(height) - 1
    maxarea = 0

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        maxarea = max(maxarea, area)

        # update pointers by shifting the smallest height
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return maxarea


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
