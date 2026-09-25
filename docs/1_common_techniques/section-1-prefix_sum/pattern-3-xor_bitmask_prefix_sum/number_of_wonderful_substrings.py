from collections import defaultdict

class Solution:
    def wonderful_substrings(self, word: str) -> int:
        d = [0] * 1024
        d[0] = 1
        mask = 0
        res = 0

        for c in word:
            i = ord(c) - ord('a')
            mask ^= (1 << i)
            res += d[mask]

            for j in range(10):
                res += d[mask ^ (1 << j)]
            
            d[mask] += 1
        
        return res


word = "aba"
print(Solution().wonderfulSubstrings(word))