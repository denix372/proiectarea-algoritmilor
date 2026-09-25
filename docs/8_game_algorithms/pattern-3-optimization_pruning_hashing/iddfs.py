import time
import math
from typing import List, Any

# Mock classes to simulate a generic board game (like Chess or Checkers)
class Move:
    def __init__(self, name: str):
        self.name = name
    def __repr__(self): return self.name

class GameState:
    def __init__(self, identifier: str, is_terminal: bool = False, heuristic_val: float = 0.0):
        self.id = identifier
        self.is_terminal = is_terminal
        self.heuristic_val = heuristic_val
        self.children = [] # List of tuples: (Move, GameState)
        
    def get_legal_moves(self) -> List[Move]:
        return [move for move, state in self.children]
        
    def apply_move(self, move: Move) -> 'GameState':
        for m, state in self.children:
            if m.name == move.name:
                return state
        return self
        
    def evaluate(self) -> float:
        # The Heuristic Evaluation Function
        # Instead of absolute Win/Loss (+inf, -inf), it returns an estimation 
        # (e.g., piece advantage in Chess, board control in Go).
        return self.heuristic_val

class IterativeDeepeningAI:
    def __init__(self, time_limit_seconds: float):
        self.time_limit = time_limit_seconds
        self.start_time = 0.0
        self.time_expired = False
        
    def _is_time_up(self) -> bool:
        if time.time() - self.start_time > self.time_limit:
            self.time_expired = True
            return True
        return False

    # Standard Alpha-Beta (Negamax variant) augmented with Time Checking
    def _negamax(self, state: GameState, depth: int, alpha: float, beta: float, color: int) -> float:
        # 1. Time Check: If time is up, abort search and bubble up immediately.
        if self._is_time_up():
            return 0.0
            
        # 2. Base Case: Max depth reached or game is over. 
        # We rely on the Heuristic Evaluation Function here.
        if depth == 0 or state.is_terminal:
            return color * state.evaluate()
            
        best_value = -math.inf
        
        # 3. Recursive Alpha-Beta Search
        for move in state.get_legal_moves():
            next_state = state.apply_move(move)
            
            # Negamax trick: swap perspectives by negating the recursive call
            # and swapping alpha/beta boundaries.
            val = -self._negamax(next_state, depth - 1, -beta, -alpha, -color)
            
            # If time expired deeply in recursion, discard this incomplete evaluation
            if self.time_expired:
                return 0.0
                
            best_value = max(best_value, val)
            alpha = max(alpha, best_value)
            
            # Pruning
            if alpha >= beta:
                break
                
        return best_value

    def get_best_move(self, initial_state: GameState) -> Move:
        self.start_time = time.time()
        self.time_expired = False
        
        best_move = None
        current_depth = 1
        
        # 4. ITERATIVE DEEPENING LOOP
        # Progressively search deeper (Depth 1, then 2, then 3...) until time runs out.
        while not self.time_expired:
            current_best_move = None
            best_value = -math.inf
            alpha = -math.inf
            beta = math.inf
            
            moves = initial_state.get_legal_moves()
            if not moves:
                break
                
            # Move Ordering could be applied here for massive Alpha-Beta optimization!
            
            for move in moves:
                next_state = initial_state.apply_move(move)
                val = -self._negamax(next_state, current_depth - 1, -beta, -alpha, -1)
                
                # If time expired during this depth search, we MUST discard the results 
                # of this entire depth level, because they are incomplete.
                if self.time_expired:
                    break
                    
                if val > best_value:
                    best_value = val
                    current_best_move = move
                
                alpha = max(alpha, best_value)
                
            # If we successfully completed the search at this depth, lock in the best move
            if not self.time_expired and current_best_move:
                best_move = current_best_move
                print(f"Depth {current_depth} completed. Current best move: {best_move.name} (Eval: {best_value})")
                
            current_depth += 1
            
        print(f"Time limit reached! Search aborted at depth {current_depth}.")
        return best_move

# --- DRIVER CODE (EXAMPLE USAGE) ---
# Constructing a mock game tree
root = GameState("Root")

# Move A leads to a quick small advantage
state_A = GameState("StateA", heuristic_val=2.0)
state_A.children = [(Move("A1"), GameState("A1_Leaf", True, 2.5)), 
                    (Move("A2"), GameState("A2_Leaf", True, 1.5))]

# Move B leads to a massive advantage, but requires searching deeper to see it
state_B = GameState("StateB", heuristic_val=-1.0)
state_B_child = GameState("StateB_Child", heuristic_val=0.0)
state_B_child.children = [(Move("B1_Deep"), GameState("B1_Deep_Leaf", True, 10.0))]
state_B.children = [(Move("B1"), state_B_child)]

root.children = [(Move("A"), state_A), (Move("B"), state_B)]

# Initialize AI with a strict time limit (e.g., 0.05 seconds for simulation)
print("--- Iterative Deepening & Heuristic Evaluation ---")
ai = IterativeDeepeningAI(time_limit_seconds=0.05)
final_move = ai.get_best_move(root)

print(f"\nFinal Chosen Move: {final_move}")
print()

'''
GAME THEORY ANALYSIS & PROOF (Iterative Deepening & Heuristics)

A) The Need for Iterative Deepening (IDDFS):
   In complex games like Chess or Go, the state space is overwhelmingly large. 
   A pure DFS (Minimax) searching to a fixed depth of 10 might take 2 seconds 
   in the endgame, but 5 hours in the midgame. 
   IDDFS solves this by searching to Depth 1, then Depth 2, then Depth 3, etc., 
   until a strict time limit (e.g., 3 seconds per turn) expires. 
   When time runs out, the AI simply uses the best move found in the LAST FULLY 
   COMPLETED depth level.

B) Isn't searching the same nodes over and over inefficient?
   Surprisingly, no! In a tree with a large branching factor 'b', the vast majority 
   of the nodes are located at the very bottom level (the leaves). 
   The time taken to search depth 1 to (d-1) combined is mathematically insignificant 
   compared to the time it takes to search depth 'd'. Thus, the overhead of IDDFS 
   is negligible, while the time-management benefits are immense.

C) Heuristic Evaluation Function:
   Since the AI rarely reaches absolute terminal states (Checkmate), it stops at 
   the current depth limit and "guesses" who is winning using a Heuristic. 
   In Chess, this function assigns points to pieces (+9 for Queen, +1 for Pawn), 
   evaluates king safety, and center board control. The accuracy of this Heuristic 
   dictates the entire intelligence of the AI.

D) Synergy with Alpha-Beta Pruning (Move Ordering):
   IDDFS provides a massive secondary benefit: The best move found at Depth(N-1) 
   is highly likely to be the best move at Depth(N). By evaluating that specific 
   move FIRST during the Depth(N) search, Alpha-Beta pruning will achieve maximum 
   efficiency, pruning huge portions of the tree immediately.
'''