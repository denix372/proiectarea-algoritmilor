
class Solution:
    def stone_game_iii(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        
        # dp[i] represents the maximum score difference the current player 
        # can achieve starting from index i.
        # We add 3 extra elements initialized to 0 to avoid out-of-bounds checks.
        dp = [0] * (n + 3)
        
        # Minimax evaluated bottom-up (from the end of the array to the beginning)
        for i in range(n - 1, -1, -1):
            take_one = stoneValue[i] - dp[i + 1]
            
            take_two = float('-inf')
            if i + 1 < n:
                take_two = stoneValue[i] + stoneValue[i + 1] - dp[i + 2]
                
            take_three = float('-inf')
            if i + 2 < n:
                take_three = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3]
                
            # The current player plays optimally to MAXIMIZE their score difference
            dp[i] = max(take_one, take_two, take_three)
            
        # The result at dp[0] holds the score difference for Alice (since she goes first)
        alice_score_diff = dp[0]
        
        if alice_score_diff > 0:
            return "Alice"
        elif alice_score_diff < 0:
            return "Bob"
        else:
            return "Tie"

stoneValue = [1,2,3,7]
print(Solution().stoneGameIII(stoneValue))

'''
GAME THEORY ANALYSIS & PROOF (Negamax with Dynamic Programming)

A) Core Mathematical Idea (Relative Score):
   In zero-sum games where players try to maximize their own points while the 
   total points are fixed, the goal is equivalent to maximizing the difference 
   in points between yourself and your opponent.
   Diff = My_Points - Opponent_Points
   When I take X points, the opponent will play optimally from the remaining 
   board and achieve a maximum difference of Next_Diff.
   Therefore, my net difference will mathematically be: X - Next_Diff.

B) The O(N) Transition (Bottom-Up Minimax):
   Instead of top-down recursion (which branches out and requires deep stacks), 
   we start from the end of the game where the board is empty (DP[n] = 0).
   For any position 'i', a player has up to 3 choices:
   - Take 1 stone : score_diff = stoneValue[i] - DP[i+1]
   - Take 2 stones: score_diff = stoneValue[i] + stoneValue[i+1] - DP[i+2]
   - Take 3 stones: score_diff = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - DP[i+3]
   
   The player will always choose the maximum of these available differences.

C) Complexity:
   - Time Complexity: O(N). We iterate through the array of length N exactly once. 
     At each step, we do a maximum of 3 constant-time operations.
   - Space Complexity: O(N) for the DP array. This can technically be optimized 
     to O(1) by only keeping track of the last 3 computed DP values.
'''