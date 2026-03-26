from heapq import heappush, heappop
class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = [False] * n
        q = []
        heappush(q, (0, 0 ))
        total_cost = 0
        edges_used = 0

        while edges_used < n:
            cost, u = heappop(q)
            if visited[u]:
                continue
            visited[u] = True
            total_cost += cost
            edges_used += 1

            x1, y1 = points[u]
            for v in range(n):
                if not visited[v]:
                    x2, y2 = points[v]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heappush(q, (dist, v))

        return total_cost

points = [[3,12],[-2,5],[-4,1]]
print(Solution().minCostConnectPoints(points))