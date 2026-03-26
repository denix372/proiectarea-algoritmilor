from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x : x[1])

        end = -1001
        count = 0
        for p in pairs:
            if end < p[0]:
                end = p[1]
                count += 1
        return count

pairs = [[1,2],[2,3],[3,4]]
print(Solution().findLongestChain(pairs))