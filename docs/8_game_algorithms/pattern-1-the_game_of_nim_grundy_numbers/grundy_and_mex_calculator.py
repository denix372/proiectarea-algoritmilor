from typing import List, Set

class SpragueGrundyTheory:
    def __init__(self, allowed_moves: List[int]):
        # The set of allowed moves (e.g., players can only remove 2, 3, or 5 stones)
        self.allowed_moves = allowed_moves
        self.memo = {}

    # MEX (Minimum Excluded value)
    def calculate_mex(self, values: Set[int]) -> int:
        mex = 0
        while mex in values:
            mex += 1
        return mex

    # Computes the Grundy Number (Nimber) for a given state
    def calculate_grundy(self, n: int) -> int:
        if n == 0:
            return 0  # Terminal state (no stones left) -> Grundy is 0
            
        if n in self.memo:
            return self.memo[n]
            
        reachable_grundy_values = set()
        
        # Transition to all possible next states
        for move in self.allowed_moves:
            if n >= move:
                next_state = n - move
                reachable_grundy_values.add(self.calculate_grundy(next_state))
                
        # The Grundy value of the current state is the MEX of all reachable states
        self.memo[n] = self.calculate_mex(reachable_grundy_values)
        return self.memo[n]

    def predict_winner(self, piles: List[int]) -> str:
        # According to the Sprague-Grundy Theorem, a game with multiple independent 
        # piles is equivalent to a single Nim pile whose size is the XOR sum of 
        # the Grundy values of each independent pile.
        xor_sum = 0
        for pile in piles:
            xor_sum ^= self.calculate_grundy(pile)
            
        # If the XOR sum is strictly greater than 0, the first player wins.
        return "Player A" if xor_sum > 0 else "Player B"

# --- DRIVER CODE (EXAMPLE USAGE) ---
# Game Rules: You can only remove 2, 3, or 5 stones from any pile.
game = SpragueGrundyTheory([2, 3, 5])
piles = [10, 12, 15]

print("--- Sprague-Grundy Theorem (Sets 1-4) ---")
print(f"Piles: {piles} | Allowed Moves: [2, 3, 5]")
print(f"Winner: {game.predict_winner(piles)}")
print()

'''
COMBINATORIAL GAME THEORY (Nimbers, MEX, & Sprague-Grundy)

A) MEX (Minimum Excluded Value):
   The MEX of a set of non-negative integers is the smallest non-negative integer 
   NOT present in the set. 
   Example: MEX({0, 1, 3}) = 2. MEX({1, 2}) = 0.

B) Grundy Numbers (Nimbers):
   In any impartial game (where available moves are the same for both players), 
   any game state can be mapped to an equivalent pile of stones in a Nim Game. 
   The size of this equivalent pile is the Grundy Number.
   Formula: G(state) = MEX({ G(next_state_1), G(next_state_2), ... })
   A state with G(x) = 0 is a losing state. G(x) > 0 is a winning state.

C) The Sprague-Grundy Theorem:
   When a game consists of multiple independent sub-games (like multiple piles), 
   the entire game can be resolved by calculating the Grundy Number of each sub-game 
   independently, and then XOR-ing them together.
   Total Game State = G(pile_1) ^ G(pile_2) ^ ... ^ G(pile_n)
   If the total XOR sum > 0, the First Player wins. Otherwise, the Second Player wins.
'''