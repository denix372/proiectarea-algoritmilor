from typing import List

class Solution:
    def isPrintable(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # 1. Bounding boxes for each color
        INF = 10**9
        minr = [INF] * 61
        maxr = [- INF] * 61
        minc = [INF] * 61
        maxc = [- INF] * 61
        
        colors = set()
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                colors.add(c)
                minr[c] = min(minr[c], i)
                maxr[c] = max(maxr[c], i)
                minc[c] = min(minc[c], j)
                maxc[c] = max(maxc[c], j)
        
        # 2. Build dependency graph: c -> d if rect(c) contains d
        graph = {c: set() for c in colors}
        indeg = {c: 0 for c in colors}
        
        for c in colors:
            for i in range(minr[c], maxr[c] + 1):
                for j in range(minc[c], maxc[c] + 1):
                    d = grid[i][j]
                    if d != c:
                        if d not in graph[c]:
                            graph[c].add(d)
                            indeg[d] += 1
        
        # 3. Topological sort (Kahn)
        from collections import deque
        q = deque([c for c in colors if indeg[c] == 0])
        cnt = 0
        
        while q:
            u = q.popleft()
            cnt += 1
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        
        # 4. If all colors processed → no cycle → valid
        return cnt == len(colors)

targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
print(Solution().isPrintable(targetGrid))