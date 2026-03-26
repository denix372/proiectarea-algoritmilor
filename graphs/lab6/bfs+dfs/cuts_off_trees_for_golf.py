from typing import List
from collections import deque

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or forest[0][0] == 0:
            return -1
            
        n, m = len(forest), len(forest[0])
        
        # 1. Find all trees and sort them by height
        trees = []
        for r in range(n):
            for c in range(m):
                if forest[r][c] > 1:
                    trees.append((forest[r][c], r, c))
                    
        # Sort so we process shortest to tallest
        trees.sort()
        
        # 2. Helper function: BFS to find shortest path from (sr, sc) to (tr, tc)
        def bfs(sr, sc, tr, tc):
            # If we are already there, it takes 0 steps
            if sr == tr and sc == tc:
                return 0
                
            q = deque([(sr, sc, 0)])
            visited = {(sr, sc)}
            
            while q:
                i, j, dist = q.popleft()
                
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    
                    if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in visited:
                        # We can walk on flat ground (1) or through ANY tree (> 1)
                        if forest[ni][nj] != 0:
                            if ni == tr and nj == tc:
                                return dist + 1
                                
                            visited.add((ni, nj))
                            q.append((ni, nj, dist + 1))
            return -1

        # 3. Traverse the forest tree by tree
        total = 0
        i, j = 0, 0
        
        for _, ti, tj in trees:
            steps = bfs(i, j, ti, tj)
            
            if steps == -1:
                return -1 # Impossible to reach the next tree
                
            total += steps
            # Move our starting position to the tree we just cut
            i, j = ti, tj
            
        return total

forest = [[1,2,3],[0,0,4],[7,6,5]]
print(Solution().cutOffTree(forest))