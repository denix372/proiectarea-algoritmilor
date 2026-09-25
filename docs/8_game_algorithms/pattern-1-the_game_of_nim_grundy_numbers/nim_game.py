
class Solution:
    def can_win_nim(self, n: int) -> bool:
        return n % 4 != 0

n = 4
print(Solution().canWinNim(n))

'''
GAME THEORY ANALYSIS & PROOF (Backward Induction)

A) Core Mathematical Idea:
   This is a classic combinatorial game known as the "Nim Game". 
   Since a player can remove 1, 2, or 3 stones, the maximum number of stones 
   that can be removed in one full round (Player A + Player B) is exactly 4.
   
B) Proof by Backward Induction:
   Let's classify states as Winning (W) or Losing (L) for the player whose turn it is.
   - Base states: 
     n = 1, 2, or 3 -> W (You can take all of them and win immediately).
     
   - n = 4 -> L
     No matter if you take 1, 2, or 3 stones, you will leave 3, 2, or 1 stones 
     for your opponent. Since 1, 2, and 3 are Winning states for them, you lose.
     
   - n = 5, 6, 7 -> W
     You can take exactly 1, 2, or 3 stones to leave exactly 4 stones for your 
     opponent. Since 4 is a Losing state for them, you secure the win.
     
   - n = 8 -> L
     You can take 1, 2, or 3 stones, leaving 7, 6, or 5 stones. Since we just 
     proved that 5, 6, and 7 are Winning states for the next player, your opponent 
     will win no matter what you do.

C) Generalization:
   - A state 'n' is a Losing state (False) if and only if n is a multiple of 4 (n % 4 == 0).
   - If n is NOT a multiple of 4 (n % 4 != 0), it is a Winning state (True) because 
     you can simply remove exactly (n % 4) stones on your first turn. This leaves 
     a multiple of 4 for your opponent, forcing them into a guaranteed Losing state.
     From then on, whatever amount 'x' they take, you just take '4 - x', keeping 
     the remaining stones a multiple of 4 until it reaches 0.

D) Complexity:
   - Time Complexity: O(1) - Evaluated in constant time using the modulo operator.
   - Space Complexity: O(1) - No extra space required.
'''