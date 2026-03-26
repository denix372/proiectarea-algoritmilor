from heapq import heappush, heappop, heapify
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        heap = [(-f, c) for c, f in freq.items()]
        heapify(heap)

        res = []

        while len(heap) > 1:
            f1, c1 = heappop(heap)
            f2, c2 = heappop(heap)

            res.append(c1)
            res.append(c2)

            if f1 + 1 < 0:
                heappush(heap, (f1 + 1, c1))
            if f2 + 1 < 0:
                heappush(heap, (f2 + 1, c2))

        if heap:
            f, c = heappop(heap)
            if -f > 1:
                return "" 
            res.append(c)

        return "".join(res)
s = "aab"
print(Solution().reorganizeString(s))