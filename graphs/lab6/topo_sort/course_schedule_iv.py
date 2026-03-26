from typing import List
from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        q = deque()
        indeg = [0] * numCourses
        adj= [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            adj[a].append(b)
            indeg[b] += 1
        
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        p = [set() for _ in range(numCourses)]
        while q:
            u = q.popleft()
            for v in adj[u]:
                p[v].add(u)
                p[v].update(p[u])
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        
        res = []
        for a, b in queries:
            res.append(a in p[b])
        return res
numCourses = 2
prerequisites = [[1,0]]
queries = [[0,1],[1,0]]
print(Solution().checkIfPrerequisite(numCourses, prerequisites, queries))