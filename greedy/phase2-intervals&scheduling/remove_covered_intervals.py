from typing import List
class Solution:
    def removeCoveredIntervals(self, A: List[List[int]]) -> int:
        A.sort(key = lambda x : (x[0], -x[1]))
        count = 0
        end = 0
        for i in A:
            if end < i[1]:
                count += 1
                end = i[1]
        return count

intervals = [[1,4],[3,6],[2,8]]
print(Solution().removeCoveredIntervals(intervals))