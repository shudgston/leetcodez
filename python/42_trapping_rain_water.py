# https://leetcode.com/problems/trapping-rain-water/

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # time=O(n), space=O(n)
        # find max_left and max_right for each position i
        # water = min(max_left, max_right) - h[i], round up to 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        max_l = 0
        max_r = 0
        res = 0

        for i in range(1, n):
            # print("i:", i)
            max_l = max(max_l, height[i - 1])
            max_left[i] = max_l

        for i in range(n - 2, -1, -1):
            max_r = max(max_r, height[i + 1])
            max_right[i] = max_r

        for i in range(n):
            # get the min(L, R)
            m = min(max_left[i], max_right[i])
            water = m - height[i]
            if water >= 0:
                res += water

        return res

    def trap2pointers(self, height: List[int]) -> int:
        # time=O(n), space=O(1)
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        max_l = height[l]
        max_r = height[r]
        res = 0

        while l < r:
            # shift pointer with smaller max value
            if max_l <= max_r:
                l += 1
                max_l = max(max_l, height[l])
                res += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                res += max_r - height[r]

        return res


# class SolutionOriginalAttempt:
#     def trap(self, height: List[int]) -> int:
#         # initial (abandoned) brute force-ish attempt
#         # for each found valley in height:
#         #     expand L and R pointer out to each L and R peak
#         #     calculate water when max peaks found

#         res = 0
#         peaks = [i for i in range(len(height)) if is_peak(height, i)]
#         print("peaks:", peaks)

#         l = peaks.pop(0)
#         while peaks:
#             r = peaks.pop(0)
#             shortest_side = min(height[l], height[r])
#             area = (r - l + 1) * shortest_side
#             water = area - (shortest_side * 2)

#             for x in range(l + 1, r):
#                 water -= height[x]

#             res += water
#             l = r

#         return res


# def is_valley(arr: list, i: int) -> bool:
#     if i == 0 or i == len(arr) - 1:
#         return False
#     if i > 0 and arr[i] > arr[i - 1]:
#         return False
#     if i < len(arr) - 1 and arr[i] > arr[i + 1]:
#         return False
#     return True


# def is_peak(arr: list, i: int) -> bool:
#     if i - 1 >= 0 and arr[i] < arr[i - 1]:
#         return False

#     if i + 1 < len(arr) and arr[i] < arr[i + 1]:
#         return False

#     return True


tests = [
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    [4, 2, 0, 3, 2, 5],
]


for t in tests:
    s = Solution()
    r = s.trap(t)
    print(r)
    r = s.trap2pointers(t)
    print(r)
