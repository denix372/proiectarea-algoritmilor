import random

def solve_n_queens_hill_climbing(n: int, max_steps: int = 1000) -> list[int]:
    def get_conflicts(r: int, c: int, current_board: list[int]) -> int:
        conflicts = 0
        for i in range(n):
            if i == r:
                continue
            # Check if queens share the same column or same diagonal
            if current_board[i] == c or abs(i - r) == abs(current_board[i] - c):
                conflicts += 1
        return conflicts

    # Random Restarts loop: if we get stuck in a local minimum, start over!
    while True:
        # 1. Start with a complete, random (and highly invalid) board state
        board = [random.randint(0, n - 1) for _ in range(n)]
        
        for _ in range(max_steps):
            # 2. Identify all queens currently attacking each other
            conflicted_rows = [r for r in range(n) if get_conflicts(r, board[r], board) > 0]
            
            # 3. Global Optimum Reached: 0 conflicts!
            if not conflicted_rows:
                return board
                
            # 4. Pick a random conflicted queen
            r = random.choice(conflicted_rows)
            
            # 5. HILL CLIMBING: Look at all columns in this row and find the one 
            #    that minimizes the heuristic (number of conflicts)
            min_conflicts = float('inf')
            best_cols = []
            
            for c in range(n):
                c_conflicts = get_conflicts(r, c, board)
                
                if c_conflicts < min_conflicts:
                    min_conflicts = c_conflicts
                    best_cols = [c]
                elif c_conflicts == min_conflicts:
                    best_cols.append(c)
                    
            # 6. Make the move (Gradient Descent step)
            board[r] = random.choice(best_cols)
            
        # If we reach here, we hit max_steps without finding a solution (stuck in local optimum).
        # The while loop will naturally trigger a Random Restart.

n = 8
solution = solve_n_queens_hill_climbing(n)
print(f"Board array (index=row, value=col): {solution}")

'''
HEURISTIC SEARCH ANALYSIS & PROOF (Min-Conflicts / Hill Climbing)

A) Core Mathematical Idea (Gradient Descent in State Space):
   Instead of searching for a path to a goal from an empty board, we start with 
   a fully populated board. Our "Elevation" or "Cost" is the total number of 
   conflicting queens. The heuristic function h(n) simply counts how many pieces 
   can attack each other.
   In every step, we pick one conflicted queen and move it to the square in its 
   row that strictly minimizes h(n). We are "climbing the hill" toward a state 
   with 0 conflicts.

B) The Local Maximum Trap & Simulated Annealing:
   Pure Hill Climbing often gets stuck in a "Local Minimum" (e.g., 2 conflicts 
   remain, but any single move increases the conflicts to 3). 
   To escape this, we use the "Random Restart" technique (resetting the board 
   entirely). Another advanced variant is Simulated Annealing, which would 
   occasionally accept a move that INCREASES conflicts just to jump out of the trap.

C) Complexity (The Magic of Min-Conflicts):
   - Time Complexity: O(N) expected time. Mathematically, the probability of 
     solving N-Queens with Min-Conflicts scales linearly. For N=1,000,000, 
     Backtracking would take millennia, but Min-Conflicts solves it in less 
     than 50 steps on average. (Note: the `get_conflicts` above takes O(N) 
     making the step O(N^2) for readability, but can be optimized to O(1) 
     using hash maps for diagonals).
   - Space Complexity: O(N) to store the board.
'''