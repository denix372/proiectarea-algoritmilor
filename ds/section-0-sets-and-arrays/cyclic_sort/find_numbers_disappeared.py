from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numbers = set(nums)
        res = []

        for n in range(1, len(nums) + 1):
            if n not in numbers:
                res.append(n)
        
        return res

class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            
            if nums[idx] > 0:
                nums[idx] *= -1

        res = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        
        return res

nums = [4,3,2,7,8,2,3,1]
print(Solution().findDisappearedNumbers(nums))
print(Solution2().findDisappearedNumbers(nums))
