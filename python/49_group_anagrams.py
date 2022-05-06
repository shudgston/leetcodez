from typing import List
from collections import defaultdict
from functools import lru_cache


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for c in word:
                # Faster to use cached result or just do the math? Its close.
                count[get_index(c)] += 1

            key = tuple(count)
            anagrams.setdefault(key, []).append(word)

        return [words for words in anagrams.values()]


@lru_cache(maxsize=26)
def get_index(char: str) -> int:
    return ord(char) - ord("a")


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
