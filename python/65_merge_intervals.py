from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sorting first is KEY
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            a = merged[-1]
            b = intervals[i]
            result = merge_interval(a, b)

            if result:
                merged[-1] = result
            else:
                merged.append(b)

        return merged


def merge_interval(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    """
    Retern a merged interval if two intervals can be merged,
    or an empty list if not
    """
    if a[1] >= b[0] or b[0] <= a[0] and b[1] >= a[1]:
        result = [min(a[0], b[0]), max(a[1], b[1])]
        return result

    return []


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))

print(Solution().merge([[1, 4], [4, 5]]))

print(Solution().merge([[1, 3]]))

print(Solution().merge([[1, 4], [5, 6]]))

print(Solution().merge([[1, 4], [0, 4]]))

print(Solution().merge([[1, 4], [0, 0]]))


# [[2,3],[4,5],[6,7],[8,9],[1,10]] => 1, 10

print(Solution().merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
