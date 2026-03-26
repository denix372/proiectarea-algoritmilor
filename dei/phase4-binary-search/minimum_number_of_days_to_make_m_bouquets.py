from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1

        def canMake(day):
            res = 0
            consec = 0
            for x in bloomDay:
                if x <= day:
                    consec += 1
                    if consec == k:
                        res += 1
                        consec = 0
                else:
                    consec = 0
            return res >= m

        left = 1
        right = max(bloomDay)

        while left <= right:
            mid = (left + right) // 2
            if canMake(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
    
bloomDay = [1,10,3,10,2]
m = 3
k = 1
print(Solution().minDays(bloomDay, m, k))