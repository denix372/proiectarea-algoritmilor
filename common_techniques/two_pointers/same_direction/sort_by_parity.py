
class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            while i < j and nums[i] % 2 == 0:
                i += 1
            while i < j and nums[j] % 2 == 1:
                j -= 1
            
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        return nums

# or
class Solution2:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        j = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        
        return nums

nums = [3,1,2,4]
print(Solution().sortArrayByParity(nums))
print(Solution2().sortArrayByParity(nums))