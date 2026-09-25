
class Solution:
    def winner_square_game(self, n: int) -> bool:
        dp = [False] * (n + 1)
        
        # We build the answers bottom-up
        for i in range(1, n + 1):
            # Try removing every perfect square <= i
            k = 1
            while k * k <= i:
                # MINIMAX LOGIC: 
                # If there is a move (k*k) that leaves the opponent in a FALSE (losing) state,
                # then our current state 'i' is mathematically a TRUE (winning) state.
                if not dp[i - k * k]:
                    dp[i] = True
                    break  # We found a winning strategy, no need to check other squares
                k += 1
                
        return dp[n]

n = 1
print(Solution().winnerSquareGame(n))

'''
GAME THEORY ANALYSIS & PROOF (Minimax & Impartial Games)

A) Core Mathematical Idea (N-Positions and P-Positions):
   This game is a finite, impartial combinatorial game played under the normal 
   play convention (the last player to move wins). 
   According to Combinatorial Game Theory, every state can be classified as:
   - P-position (Previous player wins / Losing state): A state where EVERY 
     valid move leads to an N-position.
   - N-position (Next player wins / Winning state): A state where THERE EXISTS 
     at least one valid move that leads to a P-position.
     
   The DP array strictly evaluates this: `dp[i]` is True (N-position) if there 
   is at least one valid perfect square `k*k` such that `dp[i - k*k]` is False 
   (a P-position for the opponent).

B) Proof of Optimal Substructure:
   The game has no cycles (stones strictly decrease) and is perfectly deterministic. 
   By evaluating the game from 1 to N (bottom-up), we guarantee that when evaluating 
   state 'i', all possible future states `i - k*k` have already been computed and 
   permanently classified as True or False.

C) Complexity:
   - Time Complexity: O(N * sqrt(N)). For each state from 1 to N, we iterate through 
     all valid perfect squares less than or equal to 'i'. The number of perfect 
     squares up to 'i' is exactly floor(sqrt(i)). Summing this over N gives a 
     strictly bounded time complexity of O(N * sqrt(N)).
   - Space Complexity: O(N) to store the boolean states in the DP array.
'''