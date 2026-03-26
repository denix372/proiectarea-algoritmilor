from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        actual_sum = n * (n + 1) // 2
        array_sum = sum(nums)
        
        s = set(nums)
        unique_sum = sum(s)

        missing = actual_sum - unique_sum
        duplicate = array_sum - unique_sum

        return [duplicate, missing]

nums = [1,2,2,4]
print(Solution().findErrorNums(nums))