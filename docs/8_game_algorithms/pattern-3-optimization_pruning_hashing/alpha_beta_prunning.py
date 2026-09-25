import math
from typing import List

class AlphaBetaTree:
    
    # Time Complexity: Best Case O(b^(d/2)), Worst Case O(b^d)
    # Space Complexity: O(d) where d is the depth of the tree
    def get_optimal_value(self, depth: int, node_index: int, is_maximizer: bool, 
                          values: List[int], alpha: float, beta: float, max_depth: int) -> float:
        
        # Base condition: We reached the leaf nodes
        if depth == max_depth:
            return values[node_index]
            
        if is_maximizer:
            best_val = -math.inf
            
            # Recur for left and right children (Binary Tree structure: 2 * i and 2 * i + 1)
            for i in range(2):
                val = self.get_optimal_value(depth + 1, node_index * 2 + i, False, 
                                             values, alpha, beta, max_depth)
                best_val = max(best_val, val)
                
                # Update the best guaranteed score for Maximizer
                alpha = max(alpha, best_val)
                
                # ALPHA-BETA PRUNING
                # If the Minimizer already has a better or equal option higher up the tree,
                # they will never allow us to reach this state. Stop evaluating children!
                if beta <= alpha:
                    break
                    
            return best_val
            
        else: # Minimizer's turn
            best_val = math.inf
            
            for i in range(2):
                val = self.get_optimal_value(depth + 1, node_index * 2 + i, True, 
                                             values, alpha, beta, max_depth)
                best_val = min(best_val, val)
                
                # Update the best guaranteed score for Minimizer
                beta = min(beta, best_val)
                
                # ALPHA-BETA PRUNING
                # If the Maximizer already has a better or equal option higher up the tree,
                # they will never choose the path leading here. Stop evaluating children!
                if beta <= alpha:
                    break
                    
            return best_val

tree = AlphaBetaTree()

# 8 leaf nodes mean the tree has a depth of 3 (2^3 = 8)
leaf_values = [3, 5, 6, 9, 1, 2, 0, -1]
max_depth = 3

print("--- Alpha-Beta Pruning Simulator ---")
optimal_value = tree.get_optimal_value(0, 0, True, leaf_values, -math.inf, math.inf, max_depth)
print(f"Leaf Values: {leaf_values}")
print(f"The optimal value for the Maximizer is: {optimal_value} (Expected: 5)")
print()

'''
GAME THEORY ANALYSIS & PROOF (Alpha-Beta Optimization)

A) Core Mathematical Idea (Branch Pruning):
   Alpha-Beta pruning does not change the decisions made by pure Minimax; it only 
   optimizes the calculation speed. It passes the current best guarantees (alpha 
   and beta) down the recursive calls.
   - If Maximizer knows it can get a score of at least 5 (alpha = 5).
   - It explores a new branch where Minimizer's first child returns a 2.
   - Minimizer will naturally try to minimize, meaning the final score of this 
     branch will be 2 OR LESS (beta = 2).
   - Since 2 <= 5 (beta <= alpha), the Maximizer will NEVER choose this branch. 
     Thus, evaluating the rest of the children on this branch is mathematically 
     pointless and can be safely skipped (pruned).

B) Impact on Time Complexity:
   - Pure Minimax evaluates every single node: O(b^d), where b is branching factor 
     and d is depth.
   - Worst-case Alpha-Beta: If the tree is ordered such that the worst moves are 
     always evaluated first, no pruning happens. Time Complexity remains O(b^d).
   - Best-case Alpha-Beta (Perfect Move Ordering): If the best moves are always 
     evaluated first, the algorithm prunes heavily, effectively doubling the 
     search depth in the same amount of time. Time Complexity drops to O(b^(d/2)).
     In chess, this means an AI can look 10 moves ahead instead of just 5.

C) Space Complexity:
   Space complexity remains strictly bounded by the depth of the tree O(d), as 
   we only store the current path in the recursion call stack.
'''