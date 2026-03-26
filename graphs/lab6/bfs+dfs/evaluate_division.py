from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict, deque
        g = defaultdict(list)
        for (a, b), val in zip(equations, values):
            g[a].append((b, val))
            g[b].append((a, 1/val))

        def bfs(start, end):
            if start not in g or end not in g:
                return -1.0
            
            q = deque([(start, 1.0)])
            visited = set([start])

            while q:
                u, prod = q.popleft()
                if u == end:
                    return prod

                for v, w in g[u]:
                    if v not in visited:
                        visited.add(v)
                        q.append((v, prod * w))
            return -1.0
        return [bfs(a, b) for a, b in queries]
    
sol = Solution()
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(sol.calcEquation(equations, values, queries))