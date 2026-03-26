from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(int)
        for x in s:
            d[x] += 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1

s = "leetcode"
print(Solution().firstUniqChar(s))