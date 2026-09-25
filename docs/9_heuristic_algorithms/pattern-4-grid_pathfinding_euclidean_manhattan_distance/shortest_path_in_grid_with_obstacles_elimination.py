import heapq
from typing import List

class Solution:
    def shortest_path(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # O(1) Math Optimization: If we have enough 'k' to smash through everything
        # in a direct line, the answer is just the Manhattan distance.
        manhattan_dist = (rows - 1) + (cols - 1)
        if k >= manhattan_dist:
            return manhattan_dist
            
        # h(n): Manhattan Distance to the bottom-right corner
        def heuristic(r: int, c: int) -> int:
            return (rows - 1 - r) + (cols - 1 - c)
            
        # Min-Heap stores: (f_score, steps(g_score), obstacles_eliminated, row, col)
        pq = [(heuristic(0, 0), 0, 0, 0, 0)]
        
        # State tracking: visited[(row, col)] = min_obstacles_eliminated
        # We only care about revisiting a cell if we can reach it by breaking FEWER obstacles.
        visited = {(0, 0): 0}
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while pq:
            f, steps, obs, r, c = heapq.heappop(pq)
            
            # A* guarantees that the first time we pop the goal, it's the shortest path
            if r == rows - 1 and c == cols - 1:
                return steps
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_obs = obs + grid[nr][nc]
                    
                    # 1. Must not exceed allowed obstacle eliminations (k)
                    # 2. Must be a strictly better state (arriving with fewer obstacles broken)
                    if new_obs <= k and new_obs < visited.get((nr, nc), float('inf')):
                        visited[(nr, nc)] = new_obs
                        
                        new_steps = steps + 1
                        new_f = new_steps + heuristic(nr, nc)
                        
                        heapq.heappush(pq, (new_f, new_steps, new_obs, nr, nc))
                        
        return -1

grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
k = 1
print(Solution().shortestPath(grid, k))
'''
HEURISTIC SEARCH ANALYSIS (A* in 3D State-Space)

A) State-Space Dimensionality:
   In a normal grid, a state is simply the 2D coordinate (x, y). Here, because we 
   have a budget 'k', the state becomes 3D: (x, y, obstacles_eliminated). 
   Arriving at the same cell twice is completely valid IF the second arrival used 
   fewer obstacle eliminations (saving them for later). The 'visited' hash map 
   cleverly collapses this 3D space by storing only the "best" obstacle count 
   for any (x, y) coordinate.

B) Admissible Heuristic (Manhattan):
   Because the grid only allows 4-way movement, the minimum possible steps between 
   any cell and the goal (assuming zero obstacles) is the Manhattan distance. 
   Therefore, h(n) NEVER overestimates the true cost, making A* perfectly optimal.

C) A* vs BFS (Trade-offs):
   While A* explores far fewer nodes than BFS by aiming directly at the goal, 
   managing the Priority Queue adds an O(log V) overhead per operation compared 
   to the O(1) operations of a BFS Deque. However, as the grid grows massive, 
   A*'s spatial pruning vastly outweighs the heap overhead.
'''