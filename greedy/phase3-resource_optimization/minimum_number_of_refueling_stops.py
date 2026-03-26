from typing import List
from heapq import heappush, heappop
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        h = []
        res = 0
        prev = 0
        fuel = startFuel

        for distance, gas in stations + [[target, 0]]:
            fuel -= (distance - prev)
            while h and fuel < 0:
                fuel += -heappop(h)
                res += 1
            if fuel < 0:
                return -1
            heappush(h, -gas)
            prev = distance
        return res


target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]
print(Solution().minRefuelStops(target, startFuel, stations))