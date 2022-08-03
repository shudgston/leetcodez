from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        count the freq of each n in nums
        Counter({1: 3, 2: 2, 3: 1})

        Create a list "buckets" of equal length to nums.
        - each index in the list maps to the freq. count, i.e. the value of each Counter item
        - [[], [3], [2], [1], [], []]
            0   1    2.   3.   4   5
        - iterate backwards through buckets

        """
        count = Counter(nums)
        # +1 accounts for when all numbers are the same
        buckets = [[] for k in range(len(nums) + 1)]
        res = []

        for key, ct in count.items():
            buckets[ct].append(key)

        # iterate backwards through buckets
        #   iterate through each list in buckets, appending until length k is reached
        for i in range(len(buckets) - 1, 0, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res

        return res


print(">>>", Solution().topKFrequent([1, 1, 1, 2, 2, 3], k=2))
print(">>>", Solution().topKFrequent([3, 0, 1, 0], k=1))
print(">>>", Solution().topKFrequent([-1, -1], k=1))
