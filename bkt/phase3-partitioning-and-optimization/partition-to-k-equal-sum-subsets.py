from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        nums.sort(reverse=True)

        if nums[0] > target:
            return False
        
        buckets = [0] * k

        def back(i):
            if i == len(nums):
                return True
            
            for b in range(k):
                # if the number fits in te bucket, we put it 
                if buckets[b] + nums[i] <= target:
                    buckets[b] += nums[i]
                    
                    if back(i + 1):
                        return True
                    
                    buckets[b] -= nums[i]

                # pruning: if the bucket is empty, don't try others
                if buckets[b] == 0:
                    break
            
            return False
        
        return back(0)


nums = [4,3,2,3,5,2,1]
k = 4
sol = Solution()
print(sol.canPartitionKSubsets(nums, k))