from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        sum_counts = defaultdict(int)
        total_tuples = 0
        
        for a in nums1:
            for b in nums2:
                sum_counts[a + b] += 1
                
        for c in nums3:
            for d in nums4:
                target = -(c + d)
                if target in sum_counts:
                    total_tuples += sum_counts[target]

        return total_tuples

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
print(Solution().fourSumCount(nums1, nums2, nums3, nums4))