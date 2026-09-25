
class Solution:
    def max_vowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        cnt = 0
        for i in range(k):
            if s[i] in vowels:
                cnt += 1

        res = cnt
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                cnt -= 1
            if s[i] in vowels:
                cnt += 1
            
            res = max(res, cnt)
        
        return res

s = "abciiidef"
k = 3
print(Solution().maxVowels(s, k))