from typing import List

class Solution:
    def stone_game_ii(self, piles: List[int]) -> int:
        n = len(piles)
        if n == 0:
            return 0
            
        # 1. Precompute suffix sums to quickly get total stones remaining from index i
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}
        
        # dfs(i, M) returns the maximum stones the CURRENT player can get
        # starting from index 'i' with the current limit 'M'
        def dfs(i: int, M: int) -> int:
            # Base Case 1: No stones left
            if i >= n:
                return 0
                
            # Base Case 2: If we can take ALL remaining piles, do it!
            if i + 2 * M >= n:
                return suffix_sum[i]
                
            # Check memoization table
            if (i, M) in memo:
                return memo[(i, M)]
                
            max_stones = 0
            
            # 2. MINIMAX LOGIC: Try all possible valid moves X (1 to 2M)
            for X in range(1, 2 * M + 1):
                # The opponent plays optimally from index i+X with new limit max(M, X).
                # opponent_stones is what the opponent will secure.
                opponent_stones = dfs(i + X, max(M, X))
                
                # Because it's a zero-sum allocation, whatever the opponent doesn't take, we take.
                # Our stones = (Total remaining stones from i) - (Opponent's stones)
                current_stones = suffix_sum[i] - opponent_stones
                
                max_stones = max(max_stones, current_stones)
                
            memo[(i, M)] = max_stones
            return max_stones
            
        return dfs(0, 1)

piles = [2,7,9,4,4]
print(Solution().stoneGameII(piles))

'''
GAME THEORY ANALYSIS & PROOF (Minimax with Suffix Sums)

A) Core Mathematical Idea (Zero-Sum Allocation):
   This game operates on a shared pool of resources (the remaining stones). 
   Let Total(i) be the sum of all stones from index 'i' to the end of the array.
   If the current player makes a move that leaves the game at state (next_i, next_M), 
   the opponent will play optimally to secure DFS(next_i, next_M) stones.
   Therefore, the stones secured by the current player will mathematically be:
   Current_Stones = Total(i) - DFS(next_i, next_M)

B) The Minimax / Negamax Equivalence:
   Instead of writing two separate functions for Alice and Bob, we use the fact 
    that both players share the exact same objective: maximizing their own share 
    of the remaining stones. We iterate through all valid choices of X (from 1 
    to 2M) and find the move that maximizes (Total(i) - Opponent_Stones). 
   This perfectly models the Minimax premise where the opponent is trying to 
   minimize our score by maximizing theirs.

C) Overlapping Subproblems (Memoization):
   The game state is completely defined by two variables: 'i' (current index) 
   and 'M' (current multiplier). 
   Since 1 <= N <= 100, the index 'i' can take 100 values. 'M' can never exceed N 
   (because you can't take more than N elements). Thus, there are at most O(N^2) 
   unique states.

D) Complexity:
   - Time Complexity: O(N^3). There are O(N^2) states, and for each state, we 
     iterate through at most 2M choices (which is bounded by N). 
   - Space Complexity: O(N^2) to store the states in the memoization Hash Map.
'''