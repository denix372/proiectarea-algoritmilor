from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x : (-x[0], x[1]))
        q = []
        for h, k in people:
            q.insert(k, [h, k])
        return q
        
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(Solution().reconstructQueue(people))