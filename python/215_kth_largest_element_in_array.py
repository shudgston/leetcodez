import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # O(n + klogn)
        h = [n * -1 for n in nums]
        heapq.heapify(h)
        x = 0
        for _ in range(k):
            x = heapq.heappop(h) * -1

        return x


Solution().findKthLargest([3, 2, 1, 5, 6, 4], k=2)
