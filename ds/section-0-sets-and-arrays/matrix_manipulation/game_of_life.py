from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        # Directions for the 8 neighbors
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        
        # Step 1: Calculate the next state and store it in the 2nd bit
        for i in range(m):
            for j in range(n):
                # Count live neighbors by checking the 1st bit only
                live_neighbors = 0
                for dx, dy in directions:
                    r, c = i + dx, j + dy
                    if 0 <= r < m and 0 <= c < n and (board[r][c] & 1) == 1:
                        live_neighbors += 1
                
                # Apply Conway's rules
                # If cell is currently alive
                if board[i][j] & 1: 
                    # Rule 2: Lives on if 2 or 3 neighbors
                    if live_neighbors == 2 or live_neighbors == 3:
                        board[i][j] |= 2  # Set 2nd bit to 1 (becomes binary 11)
                    # (Rules 1 & 3: Dies. We do nothing, 2nd bit remains 0 -> binary 01)
                
                # If cell is currently dead
                else: 
                    # Rule 4: Reproduction
                    if live_neighbors == 3:
                        board[i][j] |= 2  # Set 2nd bit to 1 (becomes binary 10)
                        
        # Step 2: Shift all cells to the right to transition to the next state
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Solution().gameOfLife(board)
print(board)