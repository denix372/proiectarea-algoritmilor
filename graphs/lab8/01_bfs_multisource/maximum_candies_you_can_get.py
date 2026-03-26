from typing import List
from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        q = deque()
        cnt = 0
        locked = set()

        for b in initialBoxes:
            if status[b] == 1:
                q.append(b)
            else:
                locked.add(b)

        while q:
            u = q.popleft()
            cnt += candies[u]
    
            for v in containedBoxes[u]:
                if status[v] == 1:
                    q.append(v)
                else:
                    locked.add(v)

            # 3. Process new keys we found
            for k in keys[u]:
                status[k] = 1  # Add key to our global keychain!
                
                # If we were already waiting for this box, open it!
                if k in locked:
                    q.append(k)
                    locked.remove(k) # Remove from locked so we don't open it twice

        return cnt

status = [1,0,1,0]
candies = [7,5,4,100]
keys = [[],[],[1],[]]
containedBoxes = [[1,2],[3],[],[]]
initialBoxes = [0]
print(Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes))