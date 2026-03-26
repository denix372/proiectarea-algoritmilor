from typing import List
from heapq import heappush, heappop

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:    
        courses.sort(key=lambda x: x[1])

        q = []
        current_time = 0

        for duration, lastDay in courses:
            current_time += duration
            heappush(q, -duration)

            if current_time > lastDay:
                longest = -heappop(q)
                current_time -= longest

        return len(q)

courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
print(Solution().scheduleCourse(courses))