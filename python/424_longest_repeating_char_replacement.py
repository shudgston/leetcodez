from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        l = 0
        res = 0
        most_freq = 0

        # maximize the window len
        # win_len - count_of_most_frequent <= k

        for r in range(len(s)):
            seen[s[r]] += 1
            most_freq = max(most_freq, max(seen.values()))
            # win_size = r - l + 1

            # print("most_freq", most_freq)
            # print("window_size", win_size)

            while (r - l + 1) - most_freq > k:
                print("sliding left")
                # move left
                seen[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))

        return res


# print(Solution().characterReplacement("ABABBA", k=2))
# print(Solution().characterReplacement("ABAB", k=2))
print(Solution().characterReplacement("AABABBA", k=1))
