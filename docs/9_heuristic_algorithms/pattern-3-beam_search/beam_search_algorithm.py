def beam_search(graph: dict[str, list[tuple[str, int]]], start: str, goal: str, beam_width: int) -> tuple[list[str], int]:
    # beam stores tuples of: (current_node, path_taken, accumulated_score)
    beam = [(start, [start], 0)]

    while beam:
        candidates = []

        for node, path, score in beam:
            if node == goal:
                return path, score

            for neighbor, edge_score in graph.get(node, []):
                candidates.append((neighbor, path + [neighbor], score + edge_score))

        if not candidates:
            break

        # Sort candidates by score descending (keeping highest scoring paths)
        candidates.sort(key=lambda x: x[2], reverse=True)
        
        # BEAM SEARCH LOGIC: Prune the search space to the top 'beam_width' candidates
        beam = candidates[:beam_width]

        # Early exit if the goal is inside our pruned beam
        for node, path, score in beam:
            if node == goal:
                return path, score

    return [], 0

graph = {
    'A': [('B', 8), ('C', 6), ('D', 4)],
    'B': [('E', 7), ('F', 5)],
    'C': [('G', 9), ('H', 3)],
    'D': [('I', 6)],
    'E': [], 'F': [], 'G': [], 'H': [], 'I': []
}

path, score = beam_search(graph, 'A', 'G', beam_width=2)
print(f"Best Path: {path}, Score: {score}")

'''
HEURISTIC SEARCH ANALYSIS (Beam Search Fundamentals)

A) Core Mathematical Idea:
   Beam Search is a bounded variation of Breadth-First Search (BFS). Instead of 
   keeping all nodes at the current depth in memory, it evaluates them using a 
   heuristic (or score) and strictly retains only the top 'W' (Beam Width) nodes.
   The rest of the branches are permanently pruned.

B) Complexity (The Memory Advantage):
   Let B be the branching factor (average neighbors per node) and L be the path length.
   - Standard BFS Space Complexity: O(B^L) - Grows exponentially, causing Out of Memory.
   - Beam Search Space Complexity: O(W * L) - Grows linearly, strictly controlled by W.
   - Time Complexity: O(W * B * log(W * B)) per depth level, as we generate all 
     neighbors of the 'W' nodes and sort them to find the new top 'W'.

C) Trade-off (Completeness vs. Efficiency):
   Because Beam Search aggressively discards paths that appear sub-optimal in the 
   short term, it sacrifices both completeness and optimality. It is used in domains 
   like NLP (sequence generation) where exploring the entire combinatorial space 
   is mathematically impossible.
'''