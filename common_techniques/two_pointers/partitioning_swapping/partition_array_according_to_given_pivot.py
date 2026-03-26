from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        res = [0] * n
        j = 0
        k = n - 1

        for i in range(n):
            if nums[i] < pivot:
                res[j] = nums[i]
                j += 1
        
        for i in range(n - 1, -1, -1):
            if nums[i] > pivot:
                res[k] = nums[i]
                k -= 1
            
        for i in range(j, k + 1):
            res[i] = pivot
        
        return res

nums = [9,12,5,10,14,3,10]
pivot = 10
print(Solution().pivotArray(nums, pivot))