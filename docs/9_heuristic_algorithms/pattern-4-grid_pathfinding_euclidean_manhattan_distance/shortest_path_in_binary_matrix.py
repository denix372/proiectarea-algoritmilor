import heapq

class Solution:
    def shortest_path_binary_matrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
            
        # h(n): Chebyshev Distance (optimal for 8-directional grids where diagonal cost is 1)
        # It takes the maximum of the horizontal and vertical distances to the goal.
        def heuristic(r: int, c: int) -> int:
            return max(n - 1 - r, n - 1 - c)
            
        # Min-Heap stores: (f_score, g_score, row, col)
        # Note: The problem defines path length by number of cells, so g_score starts at 1
        pq = [(1 + heuristic(0, 0), 1, 0, 0)]
        best_g = {(0, 0): 1}
        
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        while pq:
            f, g, r, c = heapq.heappop(pq)
            
            # Goal reached! A* guarantees this is the shortest path.
            if r == n - 1 and c == n - 1:
                return g
                
            # Optimization: Skip if we found a strictly better path to (r, c) earlier
            if g > best_g.get((r, c), float('inf')):
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and obstacles
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    new_g = g + 1
                    
                    # If this path is strictly better, record it and push to heap
                    if new_g < best_g.get((nr, nc), float('inf')):
                        best_g[(nr, nc)] = new_g
                        new_f = new_g + heuristic(nr, nc)
                        heapq.heappush(pq, (new_f, new_g, nr, nc))
                        
        return -1

grid = [[0,0,0],[1,1,0],[1,1,0]]
print(Solution().shortestPathBinaryMatrix(grid))

'''
HEURISTIC SEARCH ANALYSIS (A* Search & Chebyshev Distance)

A) Heuristic Selection (8-Way Movement):
   - Manhattan Distance: Assumes 4-way movement (|x1-x2| + |y1-y2|). If used here, 
     it would OVERESTIMATE the cost because diagonals allow taking shortcuts. 
     Overestimating breaks A*'s guarantee of finding the optimal path.
   - Euclidean Distance: Straight line (sqrt(x^2 + y^2)). Admissible, but involves 
     floating-point math which is computationally expensive.
   - Chebyshev Distance: The true exact cost of unhindered 8-way movement where 
     diagonals cost 1. Formula: max(|x1-x2|, |y1-y2|). It is mathematically 
     perfect (admissible and consistent) for this specific problem.

B) Complexity:
   - Time Complexity: O(N^2 * log(N^2)) in the worst case (e.g., heavily winding maze). 
     However, in open spaces, A* heavily outperforms BFS because the heuristic 
     prunes branches moving away from the goal.
   - Space Complexity: O(N^2) to store the heap and the best_g tracking dictionary.
'''