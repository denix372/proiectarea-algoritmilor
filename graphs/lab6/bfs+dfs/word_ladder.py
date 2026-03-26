from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        
        if endWord not in word_set:
            return 0
            
        q = deque([(beginWord, 1)])
        
        while q:
            u, length = q.popleft()
            
            if u == endWord:
                return length

            for i in range(len(u)):
                for char_code in range(97, 123): # 'a' to 'z'
                    char = chr(char_code)
                    
                    if char == u[i]:
                        continue
    
                    v = u[:i] + char + u[i+1:]

                    if v in word_set:
                        word_set.remove(v) # Removing acts as marking it "visited"
                        q.append((v, length + 1))            
        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution().ladderLength(beginWord, endWord, wordList))