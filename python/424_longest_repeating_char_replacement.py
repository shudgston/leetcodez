from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] += 1

            if (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result


print(Solution().characterReplacement("ABABBA", k=2))
# print(Solution().characterReplacement("ABAB", k=2))
