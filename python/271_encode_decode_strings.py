# https://leetcode.com/problems/encode-and-decode-strings/

from typing import List


DELIM = "%"
DELIM_LEN = len(DELIM)


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
        i = j = 0

        while i < len(s):
            if s[i].isdigit():
                j = i + 1

                while s[j] != DELIM:
                    j += 1

                word_len = int(s[i:j])
                num_len = j - i
                result.append(
                    s[i + num_len + DELIM_LEN : i + word_len + num_len + DELIM_LEN]
                )
                i = i + word_len + num_len + DELIM_LEN

            else:
                i += 1

        return result


# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.decode(codec.encode(["Hellooo7ooX", "World"])))
