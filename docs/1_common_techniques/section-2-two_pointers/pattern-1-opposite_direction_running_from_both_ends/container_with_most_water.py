from typing import List
class Solution:
    def max_area(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:

            max_area = max(max_area, (j - i) * min(height[i], height[j]))
            if height[i] > height[j]:
                j -=1
            else:
                i += 1
    
        return max_area

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea())