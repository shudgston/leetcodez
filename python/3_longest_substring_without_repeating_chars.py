# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            # A duplicate was found. Remove s[left] from set of seen chars,
            # and advance the left pointer
            while s[right] in seen:
                if s[left] in seen:
                    seen.remove(s[left])
                    print("removing", s[left])
                left += 1

            seen.add(s[right])
            longest = max(longest, (right - left) + 1)

        return longest


strings = [
    "abcabcbb",
    "bbbbbbbb",
    "pwwkew",
    " ",
    "au",
]

for s in strings:
    print(f"input: '{s}'")
    print(Solution().lengthOfLongestSubstring(s))
