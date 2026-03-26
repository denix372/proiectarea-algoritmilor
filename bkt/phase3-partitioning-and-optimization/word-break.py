from typing import List
from functools import lru_cache

# Note that the problem can be solved using DP
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)

        @lru_cache(None)
        def back(i):
            if i == n:
                return True
            
            prefix = ""
            for j in range(i, n):
                prefix += s[j]

                if prefix in words and back(j + 1):
                    return True
            return False
    
        return back(0)


s = "leetcode"
dictionary = {"leet", "code"}
print(Solution().wordBreak(s, dictionary))