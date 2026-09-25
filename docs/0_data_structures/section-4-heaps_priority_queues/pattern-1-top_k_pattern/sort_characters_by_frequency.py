from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def frequency_sort(self, s: str) -> str:
        d = defaultdict(int)
        for x in s:
            d[x] += 1
        
        q = []
        for x, v in d.items():
            heappush(q, (-v, x))
        res = ""
        while q:
            v, x = heappop(q)
            res += x * (- v)
        return res

s = "tree"
print(Solution().frequencySort(s))