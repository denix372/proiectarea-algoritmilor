from typing import List
from heapq import heappush, heappop
MOD = 10**9 + 7
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = sorted(zip(efficiency, speed), reverse = True)
        q = []
        speed = 0
        best = 0

        for eff, spd in engineers:
            heappush(q, spd)
            speed += spd

            if len(q) > k:
                speed -= heappop(q)
            best = max(best, speed * eff)
        return best % MOD


n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2
print(Solution().maxPerformance( n, speed, efficiency, k))