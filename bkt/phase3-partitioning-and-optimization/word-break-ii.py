from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordSet = set(wordDict)
        n = len(s)

        def back(i, sol):
            if i == n:
                res.append(" ".join(sol))
                return
            
            prefix = ""
            for j in range(i, n):
                prefix += s[j]
    
                if prefix in wordDict:
                    sol.append(prefix)
                    back(j + 1, sol)
                    sol.pop()
        back(0, [])
        return res
            

s = "pineapplepenapple"
wordDict = ["apple","pen","applepen","pine","pineapple"]
sol = Solution()
print(sol.wordBreak(s, wordDict))