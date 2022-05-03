# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "}": "{", "]": "["}

        for symbol in s:
            if symbol in pairs:
                # its a closing paren
                # only peak and pop if the stack isn't empty
                if stack and stack[-1] == pairs[symbol]:
                    stack.pop()
                else:
                    return False
            else:
                # its an opening paren, assuming its a valid char
                stack.append(symbol)

        return len(stack) == 0
