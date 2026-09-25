
class Solution:
    def num_subarray_product_less_than_k(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
    
        j = 0
        p = 1
        res = 0
        for i in range(len(nums)):
            p *= nums[i]
            while p >= k:
                p //= nums[j]
                j += 1

            res +=  i - j + 1

        return res

nums = [10,5,2,6]
k = 100
print(Solution().numSubarrayProductLessThanK(nums, k))