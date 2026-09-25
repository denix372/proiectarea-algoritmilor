
class Solution:
    def stone_game(self, piles):
        return True

piles = [5, 3, 4, 5]
print(Solution().stoneGame(piles))

'''
GAME THEORY ANALYSIS & PROOF (Parity Strategy)

A) Core Mathematical Idea (Even vs Odd Indexing):
   The problem guarantees two crucial constraints:
   1. The total number of piles (N) is EVEN.
   2. The total sum of stones is ODD (ties are impossible).

   Let's label the indices of the piles as Even (0, 2, 4...) and Odd (1, 3, 5...).
   Because N is even, the array always starts with an Even index (0) and ends 
   with an Odd index (N-1).

B) The Forced Choice (Alice's Strategy):
   Before making her first move, Alice mentally calculates the sum of all stones 
   on Even indices, and the sum of all stones on Odd indices. Since the total 
   sum is odd, these two sums cannot be equal. One MUST be strictly greater.
   
   - Suppose the Even sum is greater. Alice takes the stone at index 0 (Even).
     Now the remaining array spans from index 1 (Odd) to index N-1 (Odd).
     Bob is FORCED to take an Odd-indexed pile. 
     Whether Bob takes the left or right pile, he exposes a new Even-indexed 
     pile for Alice.
   - Alice simply repeats this mirroring strategy. She will collect 100% of the 
     Even-indexed piles, and Bob will collect 100% of the Odd-indexed piles.
     
   Since Alice pre-calculated that the Even sum is greater, she mathematically 
   guarantees her victory. The exact same logic applies if she chooses the Odd sum.

C) Complexity:
   - Time Complexity: O(1). No simulation or DP is required because the constraints 
     mathematically guarantee a win for the first player.
   - Space Complexity: O(1).
'''