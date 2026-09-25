
class Solution:
    def four_sum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = []
        for a in range(len(nums)):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, len(nums)):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                    
                c = b + 1
                d = len(nums) - 1
                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]

                    if total > target:
                        d -= 1
                    elif total < target:
                        c += 1
                    else:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1

                        while nums[c] == nums[c - 1] and c < d:
                            c += 1
        return res

nums = [1,0,-1,0,-2,2]
target = 0
print(Solution().fourSum(nums, target))