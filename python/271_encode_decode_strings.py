# https://leetcode.com/problems/encode-and-decode-strings/

from typing import List

DELIM = "#"


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        res = ""

        for s in strs:
            res += str(len(s)) + DELIM + s
            # "Hello" -> "5#Hello"

        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        l = 0
        res = []

        while l < len(s):
            # "5#Hello5#World"
            r = l

            while s[r] != DELIM:
                r += 1

            wordlen = int(s[l:r])
            wordend = r + wordlen + 1
            line = s[r + 1 : wordend]
            res.append(line)
            l = wordend

        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
codec = Codec()
print(codec.decode(codec.encode(["Hellooooo0o0o0o0o0o0o0o0ooX", "World"])))
