"""
https://leetcode.com/problems/minimum-window-substring/

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


A D O B E C O D E B A N C
|         |


B B A A, ABA

"""

import collections
from itertools import count


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        tcount = collections.Counter(t)
        current = collections.defaultdict(int)
        have = 0
        need = len(tcount)
        result = (-1, -1)
        result_len = float("infinity")
        l = 0

        for r in range(len(s)):
            char = s[r]
            current[char] += 1
            if char in tcount and current[char] == tcount[char]:
                have += 1

            while have == need:
                if (r - l + 1) < result_len:
                    result = (l, r)
                    result_len = r - l + 1

                # remove from L, shrinking the window
                current[s[l]] -= 1
                if s[l] in tcount and current[s[l]] < tcount[s[l]]:
                    have -= 1
                l += 1

        if result_len != float("infinity"):
            return s[result[0] : result[1] + 1]

        return ""


tests = [
    # ("ADOBECODEBANC", "ABC"),
    # ("a", "a"),
    # ("a", "aa"),
    # ("a", "b"),
    # ("ab", "a"),  # expected: "a"
    # ("aa", "aa"),  # expected: "aa"
    ("bbaa", "aba"),  # expected: aa  # expected: "baa"
]

for args in tests:
    print(f"output: '{Solution().minWindow(*args)}'")
