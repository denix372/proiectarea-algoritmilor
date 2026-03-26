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
    
numCourses = 2
prerequisites = [[1,0],[0,1]]
sol = Solution()
print(sol.canFinish(numCourses, prerequisites))