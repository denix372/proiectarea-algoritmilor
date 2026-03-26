from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        s = e =  0
        rooms = max_rooms = 0

        while s < len(intervals):
            if starts[s] < ends[e]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                s += 1
            else:
                rooms -= 1
                e += 1
        return max_rooms

intervals =[[7,10],[2,4]]
print(Solution().eraseOverlapIntervals(intervals))