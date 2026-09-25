from typing import List

class Solution:
    def ladder_length(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        beam_width: int = 300
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
            
        # Heuristic function h(n): Hamming distance (number of differing characters)
        def heuristic(word: str) -> int:
            return sum(1 for c1, c2 in zip(word, endWord) if c1 != c2)
        
        # The beam stores tuples of (current_word, current_path_length)
        current_beam = [(beginWord, 1)]
        
        while current_beam:
            next_level_candidates = []
            
            for word, length in current_beam:
                if word == endWord:
                    return length
                    
                # Generate all valid neighbors (differing by exactly one letter)
                for i in range(len(word)):
                    for char_code in range(97, 123):  # 'a' to 'z'
                        c = chr(char_code)
                        if c == word[i]:
                            continue
                            
                        next_word = word[:i] + c + word[i+1:]
                        if next_word in word_set:
                            next_level_candidates.append(next_word)
            
            if not next_level_candidates:
                return 0
                
            # Remove duplicates from candidates
            next_level_candidates = list(set(next_level_candidates))
            
            # Sort all candidates by how close they look to the target (h(n))
            next_level_candidates.sort(key=heuristic)
            
            # BEAM SEARCH LOGIC: Keep ONLY the top 'B' (beam_width) candidates
            current_beam = []
            for next_word in next_level_candidates[:beam_width]:
                current_beam.append((next_word, length + 1))
                word_set.remove(next_word)  # Mark as visited to prevent cycles
                
        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution().ladderLength(beginWord, endWord, wordList))

'''
HEURISTIC SEARCH ANALYSIS (Beam Search)

A) Core Mechanism (Memory-Bounded Search):
   Standard BFS explores the state space level by level, keeping ALL valid nodes 
   in memory. For problems like sequence generation in NLP or massive graphs, 
   the queue size grows exponentially, leading to Out-Of-Memory (OOM) errors.
   Beam Search solves this by applying a heuristic (in this case, Hamming Distance 
   to the target word) and keeping only the top 'B' (beam width) most promising 
   nodes at each level.

B) Heuristic Used (Hamming Distance):
   The evaluation function h(n) simply counts how many letters in the current 
   word differ from the 'endWord'. A word like 'dog' has a Hamming distance of 1 
   from 'cog', making it highly favorable to be kept in the beam.

C) Vulnerabilities (Loss of Completeness):
   Because Beam Search aggressively prunes nodes that don't look immediately 
   promising, it is neither COMPLETE nor OPTIMAL. If the true shortest path 
   requires taking a step that temporarily looks "worse" (increasing the Hamming 
   distance), a narrow Beam Width will discard it, potentially failing to find 
   a solution entirely.
'''