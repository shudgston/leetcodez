from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest_sequence = 0
        # visualize:
        # 1,2,3,4,......100,.....200
        # sequence starts where number N has no adjacent N-1

        for n in seen:
            if n - 1 not in seen:
                # this is the beginning of a sequence
                # print("found sequence start", n)
                current = n
                current_sequence = 1

                # try to expand the sequence
                while current + 1 in seen:
                    current += 1
                    current_sequence += 1
                    # print("  expand to", current, "len:", current_sequence)

                longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence


print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2, 201]))
