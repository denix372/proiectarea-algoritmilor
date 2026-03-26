from typing import List
INF = 10**9
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        ans = 0
        for i in range( 1 << n):
            g = [[INF] * n for _ in range(n)]
            for x, y, w in roads:
                if ((i >> x) & 1) and ((i >> y) & 1):
                    g[x][y] = min(g[x][y], w)
                    g[y][x] = min(g[y][x], w)

            for j in range(n):
                g[j][j] = 0

            for p in range(n):
                for q in range(n):
                    for k in range(n):
                        g[q][k] = min(g[q][k], g[q][p] + g[p][k])
            ok = 1
            for j in range(n):
                for k in range(n):
                    if ((i >> j) & 1) and ((i >> k) & 1):
                        if g[j][k] > maxDistance:
                            ok = 0
                            break
                if ok == 0:
                    break
            ans += ok
        return ans
n = 3
maxDistance = 5
roads = [[0,1,2],[1,2,10],[0,2,10]]
print(Solution().numberOfSets(n, maxDistance, roads))