from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        color = [0] * numCourses # 0 = white nodes

        def dfs(u):
            if color[u] == 1:  # 1 = gray nodes
                return False

            if color[u] == 2: # 2 = black nodes
                return True

            color[u] = 1 # gray = searching node

            for v in graph[u]:
                if not dfs(v):
                    return False
            
            color[u] = 2 # black = search ended
            return True

        for i in range(numCourses):
            if color[i] == 0:
                if not dfs(i):
                    return False
        return True
    
from collections import deque
class Solution2:
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        indeg = [0] * n
        
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)
            indeg[b] += 1

        
        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
                
        cnt = 0
        while q:
            u = q.popleft()
            cnt += 1
        
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        if cnt == numCourses:
            return True
        return False
        
    
numCourses = 2
prerequisites = [[1,0],[0,1]]
sol = Solution()
sol2 = Solution2()
print(sol.canFinish(numCourses, prerequisites))
print(sol2.canFinish2(numCourses, prerequisites))
