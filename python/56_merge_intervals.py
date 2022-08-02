"""
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


1 - 3
- 2 - - - 6

1 3
2 6

if a[1] >= b[0]
    # merge, taking the max of a[1], b[1]

"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            # always look at last item in merged
            a = merged[-1]
            b = intervals[i]

            if a[1] >= b[0]:
                # do the merge
                merged[-1][1] = max(a[1], b[1])
            else:
                merged.append(b)

        return merged


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
