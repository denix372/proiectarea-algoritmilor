
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_to_bit = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        d = [-2] * 32
        d[0] = -1

        mask = 0
        max_len = 0

        for i, c in enumerate(s):
            if c in vowel_to_bit:
                mask ^= (1 << vowel_to_bit[c])
            
            if d[mask] != -2:
                max_len = max(max_len, i - d[mask])
            else:
                d[mask] = i
        
        return max_len

s = "eleetminicoworoep"
print(Solution().findTheLongestSubstring(s))