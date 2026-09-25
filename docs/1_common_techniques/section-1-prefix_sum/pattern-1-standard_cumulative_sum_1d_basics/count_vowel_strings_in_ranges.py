from typing import List

class Solution:
    def vowel_strings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        prefix = [0] * (n + 1)
        for i in range(n):
            if words[i][0] in 'aeiou' and words[i][-1] in 'aeiou':
                prefix[i + 1] = prefix[i] + 1
            else:
                prefix[i + 1] = prefix[i]
        
        res = []
        for l, r in queries:
            res.append(prefix[r + 1] - prefix[l])
        
        return res

words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]
print(Solution().vowelStrings(words, queries))