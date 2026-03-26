from typing import List
INF = 10**9 + 1
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        dp = [[-INF] * (n + 1) for _ in range(n + 1)]

        dp[0][0] = startFuel

        for i in range(1, n + 1):
            pos, fuel = stations[i - 1]

            for j in range(0, i + 1):
                dp[i][j] = dp[i - 1][j]

                if j > 0 and dp[i - 1][j - 1] >= pos:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + fuel)

        for j in range(n + 1):
            if dp[n][j] >= target:
                return j
        return -1

target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]
print(Solution().minRefuelStops(target, startFuel, stations))