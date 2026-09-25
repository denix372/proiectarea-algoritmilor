
def find_the_winner(k: int, n: int) -> str:
    return "Player2" if n % (k + 1) == 0 else "Player1"

k, n = 7, 50
print(find_the_winner(k, n))

'''
GAME THEORY ANALYSIS & PROOF (Modulo Cycle Strategy)

A) Core Mathematical Idea:
   This is the classic Bachet's Game. Players can subtract any value from 1 to K. 
   The sum of the minimum and maximum possible moves naturally forms a cycle of (K + 1). 
   If a player is left with exactly (K + 1) remaining, any move they make (subtracting X) 
   will leave exactly (K + 1) - X remaining. 
   Since (K + 1) - X is always perfectly within the range [1, K], the opponent can 
   immediately take the rest and win. 
   Conclusion: Any multiple of (K + 1) is a forced losing state (P-position).

B) Optimal Strategy:
   - If N % (K + 1) == 0: Player 1 starts in a losing state. Whatever Player 1 
     subtracts, Player 2 can subtract the complement to complete the (K + 1) cycle.
   - If N % (K + 1) != 0: Player 1 starts in a winning state. Player 1 subtracts 
     exactly N % (K + 1) on their first turn, leaving Player 2 with a perfect 
     multiple of (K + 1), sealing the victory.

C) Complexity:
   - Time Complexity: O(1). The winner is found instantly via modulo operation.
   - Space Complexity: O(1).
'''