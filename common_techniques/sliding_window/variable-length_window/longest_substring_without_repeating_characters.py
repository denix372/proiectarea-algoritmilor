
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        k = 0
        res = 0
        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[k])
                k += 1
            
            window.add(s[i])
            res = max(res, i - k + 1)
        return res

s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))