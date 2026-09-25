from typing import List

class Solution:
    def predict_the_winner(self, nums: List[int]) -> bool:
        memo = {}

        def get_max_diff(left: int, right: int) -> int:
            if left == right:
                return nums[left]
                
            if (left, right) in memo:
                return memo[(left, right)]
                
            # Option 1: Take the left element.
            # We gain nums[left], but the opponent will play optimally on the remaining array. So we SUBTRACT the opponent's best possible score difference.
            pick_left = nums[left] - get_max_diff(left + 1, right)
            
            # Option 2: Take the right element.
            pick_right = nums[right] - get_max_diff(left, right - 1)
            
            # The current player plays optimally, so they choose the MAXIMUM of the two options
            memo[(left, right)] = max(pick_left, pick_right)
            return memo[(left, right)]

        # Player 1 wins if their final score difference is >= 0
        return get_max_diff(0, len(nums) - 1) >= 0

nums = [1,5,2]
print(Solution().predictTheWinner(nums))

'''
GAME THEORY ANALYSIS & PROOF (Minimax & Negamax Algorithm)

A) Core Mathematical Idea (Zero-Sum Game as Score Difference):
   Instead of tracking Player 1 and Player 2 scores separately, we track the 
   relative advantage: `Diff = Score(Current) - Score(Opponent)`.
   If Player 1 starts the game and achieves a final Diff >= 0, they win.
   
   This transforms the standard Minimax (where we need separate logic for the 
   Maximizer and Minimizer) into the elegant "Negamax" formulation:
   Both players attempt to maximize their own score difference. When Player A 
   makes a move, the remaining game is played by Player B. Player B's maximum 
   advantage is exactly Player A's disadvantage.
   Thus: `Best_Move = MAX(Choice - Negamax(Remaining_Game))`

B) Overlapping Subproblems (Dynamic Programming):
   In a pure Minimax tree, the time complexity would be O(2^N) because every 
   turn splits into 2 choices. 
   However, taking the "left then right" elements leaves the exact same sub-array 
   as taking "right then left". By memoizing the boundaries (left, right) in a 
   hash map or 2D array, we avoid re-evaluating the same game states.

C) Complexity:
   - Time Complexity: O(N^2). There are exactly N*(N+1)/2 possible sub-arrays 
     (combinations of left and right indices). Since each state evaluates in O(1) 
     using the memoized results, the total time is bounded by O(N^2).
   - Space Complexity: O(N^2) for the memoization table (Hash Map) and O(N) 
     for the recursion stack. Total Space: O(N^2).
'''