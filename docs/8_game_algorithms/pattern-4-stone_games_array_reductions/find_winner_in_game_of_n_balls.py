
def nim_game(N: int, A: int, B: int):
    # The game cycle is defined by the sum of the minimum and maximum allowed moves
    cycle_length = A + B
    
    # If the remainder is strictly less than A, the current player 
    # doesn't have enough balls to make a valid move.
    if N % cycle_length < A:
        return "Bob"
    else:
        return "Alice"


N = 3
A = 1
B = 2
print(NimGame(N, A, B))

'''
GAME THEORY ANALYSIS & PROOF (Modulo Arithmetic in Bachet's Game)

A) Core Mathematical Idea (The Magical Cycle A + B):
   Suppose there are exactly (A + B) balls on the table.
   If Player 1 removes 'X' balls (where A <= X <= B), the number of remaining 
   balls will be (A + B) - X.
   Because X is at most B, the remaining balls are AT LEAST A.
   Because X is at least A, the remaining balls are AT MOST B.
   Therefore, the remaining balls perfectly fall into the allowed range [A, B].
   This means Player 2 can ALWAYS remove the exact remaining amount and leave 
   0 balls, instantly winning.
   Conclusion: Any multiple of (A + B) is a mathematical P-position (Losing State).

B) Reducing the Game (Modulo Operation):
   Since any multiple of (A + B) guarantees a win for the player who didn't 
   start that cycle, the optimal strategy for any player is to force the opponent 
   into a multiple of (A + B).
   We can evaluate the initial state by taking N modulo (A + B).
   Let R = N % (A + B).
   
C) Winning and Losing States:
   - If R < A: The current player cannot even make a minimum valid move (A) to 
     reach a multiple of (A + B). They are stuck in a Losing State.
   - If A <= R <= B: The current player can simply remove exactly R balls on 
     their first turn. This leaves the opponent with a perfect multiple of (A + B), 
     forcing them into a permanent Losing State.
     
D) Complexity:
   - Time Complexity: O(1). The winner is determined instantly using modulo arithmetic, 
     completely bypassing the O(N * N!) complexity of a naive Sprague-Grundy DFS.
   - Space Complexity: O(1).
'''