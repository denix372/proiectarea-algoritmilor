from collections import defaultdict
class Solution:
    def getMaxOccuringChar(self, s):
        # code here
        d = defaultdict(int)
        for x in s:
            d[x] += 1
        mx = max(d.values())
        res = [x for x in d.keys() if d[x] == mx]
        return min(res)

s = "testsample"
print(Solution().getMaxOccuringChar(s))
    