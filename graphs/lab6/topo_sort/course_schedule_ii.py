from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = [[] for c in range(numCourses)]
        for a, b in prerequisites:
            prereq[b].append(a)

        output = []
        color = [0] * numCourses
        def dfs(u):
            if color[u] == 1:
                return False
            if color[u] == 2:
                return True

            color[u]  = 1
            for v in prereq[u]:
                if dfs(v) == False:
                    return False
            color[u] = 2
            output.append(u)
            return True
        
        for c in range(numCourses):
            if color[c] == 0:
                if dfs(c) == False:
                    return []
        return output[::-1]

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(Solution().findOrder(numCourses, prerequisites))