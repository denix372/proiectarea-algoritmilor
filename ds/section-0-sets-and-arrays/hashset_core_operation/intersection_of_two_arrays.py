from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        n1 = set(nums1)
        for x in nums2:
            if x in n1 and x not in res:
                res.add(x)
        return list(res)

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(Solution().intersection(nums1, nums2))