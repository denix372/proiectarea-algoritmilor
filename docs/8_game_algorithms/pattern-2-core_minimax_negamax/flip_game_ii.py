def can_win(currentState: str) -> bool:
    memo = {}

    def dfs(state: str) -> bool:
        # 1. Check if we have already evaluated this exact game state
        if state in memo:
            return memo[state]

        # 2. Try every possible valid move ("++" -> "--")
        for i in range(len(state) - 1):
            if state[i:i + 2] == "++":
                
                # Make the move by creating the next state string
                next_state = state[:i] + "--" + state[i + 2:]
                
                # 3. Game Theory Magic: 
                # If this move forces the opponent into a losing state, WE win!
                if not dfs(next_state):
                    memo[state] = True
                    return True

        # 4. If no moves force the opponent to lose, this is a losing state.
        memo[state] = False
        return False

    # Start the recursive search
    return dfs(currentState)

s = "++++"
print(canWin(s))

'''
GAME THEORY ANALYSIS & PROOF (State Space Search & Sprague-Grundy)

A) Core Mathematical Idea (N-Positions and P-Positions):
   In Combinatorial Game Theory, an impartial game under normal play convention 
   can be divided into winning states (N-positions, Next player wins) and 
   losing states (P-positions, Previous player wins).
   - A state is a WINNING state if there exists AT LEAST ONE valid move to a losing state.
   - A state is a LOSING state if ALL valid moves lead to a winning state.
   Our recursive algorithm exactly models this logic: `if not dfs(next_state): return True`.

B) Time Complexity Analysis (Memoization):
   Without memoization, the time complexity is roughly O(N!!), a double factorial, 
   because at each step we reduce the number of '+' by 2.
   WITH memoization, the number of possible states is bounded by 2^N (since each 
   character is either '+' or '-'). 
   String slicing takes O(N), so the overall Time Complexity is bounded by O(N * 2^N).
   Space Complexity is O(2^N) to store the states in the Hash Map.

C) The Ultimate Optimization (Sprague-Grundy Theorem in O(N)):
   While the DFS+Memoization is expected in interviews, this game can actually be 
   solved in O(N) using Sprague-Grundy. 
   Notice that a "-" permanently divides the game into independent subgames of 
   consecutive "+"s. 
   For example, "++++-+++" is two independent games: a pile of 4 and a pile of 3.
   By precomputing the Grundy Numbers (Nim-values) for lengths of consecutive "+"s 
   up to N using MEX, we can determine the winner simply by taking the XOR sum of 
   the Grundy values of each consecutive block of "+"s. 
   If XOR sum > 0, the first player wins.
'''