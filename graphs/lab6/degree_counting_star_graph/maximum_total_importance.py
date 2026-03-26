from typing import List
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        deg = [0] * n
        for a, b in roads:
            deg[a] += 1
            deg[b] += 1
        #cities sorted by degree
        cities = sorted(range(n), key = lambda x : deg[x])

        value = [0] * n
        v = 1
        for c in cities:
            value[c] = v
            v += 1
        
        total = 0
        for a, b in roads:
            total += value[a] + value[b]
        return total

sol = Solution()
n = 5
roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
print(sol.maximumImportance(n, roads))