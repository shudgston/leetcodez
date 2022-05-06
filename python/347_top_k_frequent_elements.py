from collections import Counter, defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for key, val in count.items():
            bucket[val].append(key)

        results = []

        # count backwards
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                results.append(n)

                if len(results) == k:
                    return results

        return results


def count_and_zip(nums, k):
    count = Counter(nums)
    res = sorted(
        [x for x in zip(count.values(), count.keys())],
        key=lambda x: x[0],
        reverse=True,
    )

    return [x[1] for x in res][:k]


print(">>>", Solution().topKFrequent([1, 1, 1, 2, 2, 3], k=2))

print(">>>", Solution().topKFrequent([3, 0, 1, 0], k=1))

print(">>>", Solution().topKFrequent([-1, -1], k=1))
