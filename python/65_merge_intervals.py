from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sorting first is KEY
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            a = merged[-1]
            b = intervals[i]

            if a[1] >= b[0]:
                merged[-1] = [a[0], max(a[1], b[1])]
            else:
                merged.append(b)

        return merged


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(Solution().merge([[1, 4], [4, 5]]))
print(Solution().merge([[1, 3]]))
print(Solution().merge([[1, 4], [5, 6]]))
print(Solution().merge([[1, 4], [0, 4]]))
print(Solution().merge([[1, 4], [0, 0]]))
print(Solution().merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
