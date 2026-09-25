
def check_winner(n: int, k: int) -> str:
    return "A" if n % (k + 1) != 0 else "B"

n, k = 50, 10
print(check_winner(n, k))

'''
GAME THEORY ANALYSIS & PROOF (Bachet's Game / Modulo Strategy)

A) Core Mathematical Idea (The Winning Cycle):
   The game is defined by the maximum number of cards a player can draw, K.
   The critical cycle length is (K + 1). 
   If a player is faced with exactly (K + 1) cards, they can draw between 1 and K cards. 
   Whatever number X they draw, the remaining number of cards will be exactly 
   (K + 1) - X, which perfectly falls in the range [1, K]. 
   Thus, the opponent can always take the rest and win. 
   Conclusion: Any multiple of (K + 1) is a forced losing state (P-position).

B) The Optimal Strategy:
   - If N % (K + 1) == 0: Player A starts in a losing state. Whatever A does, 
     Player B can always restore the multiple of (K + 1) on their turn, eventually winning.
   - If N % (K + 1) != 0: Player A starts in a winning state. Player A simply removes 
     exactly N % (K + 1) cards on the first turn. This forces Player B to start 
     with a perfect multiple of (K + 1), locking B into a losing sequence.

C) Complexity:
   - Time Complexity: O(1). The recursive simulation is bypassed entirely using modulo arithmetic.
   - Space Complexity: O(1).
'''