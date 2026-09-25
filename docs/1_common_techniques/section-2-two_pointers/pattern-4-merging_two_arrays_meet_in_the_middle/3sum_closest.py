
class Solution:
    def three_sum_closest(self, nums: list[int], target: int) -> int:
        nums.sort()
        best = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if abs(target - total) < abs(target - best):
                    best = total
                
                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    return total
            
        return best

nums = [-1,2,1,-4]
target = 1
print(Solution().threeSumClosest(nums, target))