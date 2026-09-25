from typing import List

class Solution:
    def stone_game_ix(self, stones: List[int]) -> bool:
        cnt0 = cnt1 = cnt2 = 0
        for x in stones:
            if x % 3 == 0:
                cnt0 += 1
            elif x % 3 == 1:
                cnt1 += 1
            else:
                cnt2 += 1
            
        if cnt0 % 2 == 0:
            return cnt1 > 0 and cnt2 > 0
        else:
            return abs(cnt1 - cnt2) > 2

stones = [2,1]
print(Solution().stoneGameIX(stones))
'''
GAME THEORY ANALYSIS & PROOF (Modulo Arithmetic & Game State)

A) Core Mathematical Idea:
   Instead of tracking exact sums, we only track the sum modulo 3.
   To avoid losing, a player must ensure the running sum modulo 3 never reaches 0.
   The game operates strictly on three frequencies: c0 (multiples of 3), 
   c1 (remainder 1), and c2 (remainder 2).

B) The Non-Zero Sequences:
   If we ignore c0 stones, there are only two valid chains of moves to avoid 
   hitting a sum divisible by 3:
   - Chain 1 (Starts with 1): 1, 1, 2, 1, 2, 1, 2...
   - Chain 2 (Starts with 2): 2, 2, 1, 2, 1, 2, 1...
   Notice that after the first two moves, the sequence perfectly alternates.

C) The Role of Multiples of 3 (c0):
   Playing a c0 stone does not change the running sum modulo 3. It acts as a 
   "Turn Skip" or "Reverse" card.
   - If c0 is EVEN: The turn skips cancel out (Player A uses one, Player B uses 
     another to counter). The game plays out as if there are no c0 stones. 
     Alice wins simply if she is able to choose the chain that benefits her. She 
     can do this as long as both c1 > 0 and c2 > 0.
   
   - If c0 is ODD: There is a net of ONE turn skip. Bob will weaponize this 
     extra skip to swap roles, making Alice face the disadvantage. To survive 
     this parity flip and force Bob to run out of stones, Alice must have an 
     overwhelming majority in either c1 or c2. Specifically, the absolute 
     difference between c1 and c2 must strictly exceed 2 (|c1 - c2| > 2).

D) Complexity:
   - Time Complexity: O(N) to iterate through the array once and count remainders.
   - Space Complexity: O(1) requiring only three integer variables.
'''