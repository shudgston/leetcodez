# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # The cheat way:
        # s = [c.lower() for c in s if c.isalnum()]
        # return s == s[::-1]
        converted = [char.lower() for char in s if char.isalnum()]
        n = len(converted)

        left = 0
        right = n - 1

        while left < right:
            if converted[left] != converted[right]:
                return False
            left += 1
            right -= 1

        return True
