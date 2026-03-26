from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        j = 0
        res = 0
        d = defaultdict(int)
        max_occ = 0

        for i in range(len(s)):
            d[s[i]] += 1
            max_occ = max(max_occ, d[s[i]])

            while (i - j + 1) - max_occ > k:
                d[s[j]] -= 1
                j += 1 

            res = max(res, i - j + 1)
        
        return res

s = "ABAB"
k = 2
print(Solution().characterReplacement(s, k))