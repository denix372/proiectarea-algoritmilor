import heapq

class Solution:
    def sliding_puzzle(self, board: list[list[int]]) -> int:
        target = "123450"
        
        # Flatten the 2D board into a 1D string for easy hashing and manipulation
        start = "".join(str(val) for row in board for val in row)
        
        if start == target:
            return 0
            
        # Precompute valid swap indices for the '0' tile in a 1D array of length 6
        # 0 1 2
        # 3 4 5
        adj_moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        # Target coordinates (row, col) for each tile '1' through '5'
        # to calculate Manhattan distance easily
        target_pos = {
            '1': (0, 0), '2': (0, 1), '3': (0, 2),
            '4': (1, 0), '5': (1, 1)
        }
        
        # Heuristic Function h(n): Sum of Manhattan distances of all tiles
        def get_manhattan(state: str) -> int:
            dist = 0
            for i, char in enumerate(state):
                if char == '0':  # We don't count the empty space
                    continue
                curr_r, curr_c = i // 3, i % 3
                tar_r, tar_c = target_pos[char]
                dist += abs(curr_r - tar_r) + abs(curr_c - tar_c)
            return dist

        # Min-Heap stores: (f_score, g_score, state_string, zero_index)
        zero_idx = start.index('0')
        pq = [(get_manhattan(start), 0, start, zero_idx)]
        
        # Track the best g_score for each state to avoid cycles
        best_g = {start: 0}
        
        while pq:
            f, g, state, z_idx = heapq.heappop(pq)
            
            # Goal reached! A* guarantees it's the minimum moves.
            if state == target:
                return g
                
            # Skip if we already found a shorter path to this exact board state
            if g > best_g.get(state, float('inf')):
                continue
                
            # Generate valid neighbors by swapping '0' with adjacent tiles
            state_list = list(state)
            for next_z in adj_moves[z_idx]:
                # Swap
                state_list[z_idx], state_list[next_z] = state_list[next_z], state_list[z_idx]
                new_state = "".join(state_list)
                # Swap back for the next iteration in the loop
                state_list[z_idx], state_list[next_z] = state_list[next_z], state_list[z_idx]
                
                new_g = g + 1
                if new_g < best_g.get(new_state, float('inf')):
                    best_g[new_state] = new_g
                    new_f = new_g + get_manhattan(new_state)
                    heapq.heappush(pq, (new_f, new_g, new_state, next_z))
                    
        return -1

board = [[1,2,3],[4,0,5]]
print(Solution().slidingPuzzle(board))
'''
HEURISTIC SEARCH ANALYSIS (State-Space Search & Dominance)

A) State Representation:
   In Grid Pathfinding, a state is just (x, y). In State-Space puzzles, the 
   ENTIRE board is the state. We flatten the 2x3 grid into a 6-character string 
   (e.g., "123405") because strings are immutable and hashable, making them 
   perfect for the 'best_g' dictionary and Priority Queue.

B) Heuristic Dominance:
   h1(n) = Misplaced Tiles
   h2(n) = Manhattan Distance
   For any state, h2(n) >= h1(n). Because A* explores fewer nodes the closer 
   the heuristic gets to the true cost, h2 DOMINATES h1. Using Manhattan distance 
   prevents the algorithm from needlessly expanding states that look "almost right" 
   (few misplaced tiles) but actually require many moves to fix.
'''