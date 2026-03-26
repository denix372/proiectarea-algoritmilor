from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2

            res = 1
            cap = 0
            for w in weights:
                if cap + w <= mid:
                    cap += w
                else:
                    res += 1
                    cap = w
                
            if res <= days:
                right = mid - 1
            else:
                left = mid + 1
            
        return left
            
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(Solution().shipWithinDays(weights, days))        
