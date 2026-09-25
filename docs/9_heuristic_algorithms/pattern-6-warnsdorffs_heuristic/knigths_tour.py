def solve_knights_tour_warnsdorff(n: int = 8) -> list[list[int]]:
    # Initialize empty board with -1
    board = [[-1] * n for _ in range(n)]
    
    # All 8 possible moves for a Knight
    directions = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    
    def is_valid_and_empty(x: int, y: int) -> bool:
        return 0 <= x < n and 0 <= y < n and board[x][y] == -1
        
    # Heuristic function: Count how many valid, unvisited neighbors a cell has
    def get_degree(x: int, y: int) -> int:
        count = 0
        for dx, dy in directions:
            if is_valid_and_empty(x + dx, y + dy):
                count += 1
        return count

    # Start from top-left corner
    curr_x, curr_y = 0, 0
    board[curr_x][curr_y] = 1
    
    # We need exactly n*n moves to complete the board
    for step in range(2, n * n + 1):
        min_degree = float('inf')
        next_x, next_y = -1, -1
        
        # Look at all valid moves from the current position
        for dx, dy in directions:
            nx, ny = curr_x + dx, curr_y + dy
            
            if is_valid_and_empty(nx, ny):
                # Apply Warnsdorff's Heuristic
                degree = get_degree(nx, ny)
                if degree < min_degree:
                    min_degree = degree
                    next_x, next_y = nx, ny
                    
        # If we couldn't find any valid move before filling the board, we are stuck
        if min_degree == float('inf'):
            return []
            
        # Make the move
        curr_x, curr_y = next_x, next_y
        board[curr_x][curr_y] = step
        
    return board

# --- DRIVER CODE ---
tour_board = solve_knights_tour_warnsdorff(8)
if tour_board:
    for row in tour_board:
        # Print formatted grid
        print("".join(f"{str(cell).rjust(3)} " for cell in row))
else:
    print("Tour failed (dead end reached).")

'''
HEURISTIC SEARCH ANALYSIS (Warnsdorff's Algorithm)

A) Domain-Specific Heuristic:
   Unlike generic heuristics like Manhattan Distance, Warnsdorff's rule is tailored 
   specifically for Knight's Tour. It calculates the "Degree" (accessibility) of 
   each potential next cell. By always moving to the cell with the MINIMUM degree, 
   the algorithm naturally gravitates toward the edges and corners early on.

B) Complexity:
   - Time Complexity: O(N^2). We make exactly N^2 jumps. At each jump, we check 
     up to 8 neighbors, and for each neighbor, we calculate its degree (checking 
     8 more neighbors). This is 64 operations per cell, which is O(1) mathematically. 
     Thus, the entire board is solved in linear time relative to its size!
   - Space Complexity: O(N^2) to store the board. No recursion stack needed!

C) Limitations:
   While Warnsdorff's rule works flawlessly for most standard board sizes (like 8x8), 
   pure Greedy implementations can occasionally hit dead ends on very large boards 
   due to tie-breaking issues (when multiple cells have the same minimum degree). 
   Advanced implementations use secondary tie-breakers (like Arnd Roth's rule).
'''