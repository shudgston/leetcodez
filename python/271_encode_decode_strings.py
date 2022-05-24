# https://leetcode.com/problems/encode-and-decode-strings/

from inspect import EndOfBlock
from typing import List


DELIM = "%"


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        result = []
        for word in strs:
            wordlen = len(word)
            result.append(str(wordlen) + DELIM + word)

        return "".join(result)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != DELIM:
                j += 1

            word_len = int(s[i:j])
            end_of_word = j + 1 + word_len
            result.append(s[j + 1 : end_of_word])
            i = end_of_word

        return result


# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.decode(codec.encode(["Hellooooo0o0o0o0o0o0o0o0ooX", "World"])))
