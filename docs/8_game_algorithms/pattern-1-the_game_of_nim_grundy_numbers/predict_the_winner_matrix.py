class MatrixRectangleGame:
    def __init__(self):
        self.memo = {}
        self.valid_masks = self._precompute_rectangle_masks()

    # Precomputes all valid rectangle bitmasks for a 4x4 grid.
    # There are (4*5/2) * (4*5/2) = 100 possible rectangles.
    def _precompute_rectangle_masks(self) -> list[int]:
        masks = []
        for r1 in range(4):
            for c1 in range(4):
                for r2 in range(r1, 4):
                    for c2 in range(c1, 4):
                        mask = 0
                        for r in range(r1, r2 + 1):
                            for c in range(c1, c2 + 1):
                                # Map 2D coordinate to 1D bit position (0 to 15)
                                mask |= (1 << (r * 4 + c))
                        masks.append(mask)
        return masks

    def _get_mex(self, values: set[int]) -> int:
        mex = 0
        while mex in values:
            mex += 1
        return mex

    # Computes Grundy number for a 16-bit integer representing the 4x4 matrix
    def _get_grundy(self, state: int) -> int:
        if state == 0:
            return 0  # Terminal state: No 1s left to select
            
        if state in self.memo:
            return self.memo[state]
            
        reachable_grundy_values = set()
        
        # Try applying every valid rectangle mask
        for mask in self.valid_masks:
            # If the mask is a perfect subset of the current state
            # (meaning all 1s in the rectangle are actually 1s in the matrix)
            if (state & mask) == mask:
                # The next state is achieved by flipping those 1s to 0s
                next_state = state ^ mask
                reachable_grundy_values.add(self._get_grundy(next_state))
                
        self.memo[state] = self._get_mex(reachable_grundy_values)
        return self.memo[state]

    def predict_winner(self, matrix: list[list[int]]) -> str:
        # Convert 2D 4x4 matrix into a single 16-bit integer
        initial_state = 0
        for r in range(4):
            for c in range(4):
                if matrix[r][c] == 1:
                    initial_state |= (1 << (r * 4 + c))
                    
        grundy_value = self._get_grundy(initial_state)
        
        # If Grundy > 0, the first player has a winning strategy
        return "Player A" if grundy_value > 0 else "Player B"

# --- DRIVER CODE (EXAMPLE USAGE) ---
game = MatrixRectangleGame()

# Example: 1s at (0,1), (0,2), (3,3)
mat1 = [
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1]
]

print("--- 4x4 Matrix Rectangle Game ---")
print(f"Winner: {game.predict_winner(mat1)} (Expected: Player A)")
print()

'''
GAME THEORY ANALYSIS & PROOF (Sprague-Grundy on 2D Matrix)

A) Core Mathematical Idea:
   This game is an impartial combinatorial game played under normal play convention 
   (last player to move wins). The game board is a 4x4 matrix, which translates 
   perfectly into a 16-bit integer state (from 0 to 65535). 

B) State Transition (Bitmasking):
   Instead of looping through matrices using strings, we precompute all 100 possible 
   rectangles in a 4x4 grid as 16-bit integer masks. 
   If a state contains a valid rectangle of 1s, the bitwise condition:
   (state & mask) == mask 
   will evaluate to True. 
   The transition to the new state is simply: next_state = state ^ mask.

C) Sprague-Grundy Application:
   For any state 'S', we compute all reachable next states. The Grundy number 
   (or Nim-value) of 'S' is the MEX (Minimum Excluded value) of the Grundy numbers 
   of all those reachable states.
   - If G(S) = 0: It is a P-position (Previous player winning / Losing state). 
     Whatever move Player A makes, Player B can guarantee a win.
   - If G(S) > 0: It is an N-position (Next player winning / Winning state). 
     Player A can make a move that leaves Player B with a state where G = 0.

D) Complexity:
   - Time Complexity: O(2^16 * R), where R is the number of valid rectangles (100).
     Since 65536 * 100 is roughly 6.5 million operations, it runs in a fraction of a 
     second, making memoization extremely efficient.
   - Space Complexity: O(2^16) to store the memoization table (the dict).
'''
