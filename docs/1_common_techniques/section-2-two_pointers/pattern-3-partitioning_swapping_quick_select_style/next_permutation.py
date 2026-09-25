
class Solution:
    def next_permutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        # 1. find first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # 2. find the element larget than nums[i] from the right
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            # 3. swap
            nums[i], nums[j] = nums[j], nums[i]
        
        # 4. reverse the suffix starting from i + 1
        i = i + 1
        j = n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
nums = [1,2,3]
Solution().nextPermutation(nums)
print(nums)