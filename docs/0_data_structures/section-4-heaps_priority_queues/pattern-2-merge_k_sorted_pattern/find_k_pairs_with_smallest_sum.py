from typing import List
from heapq import heappush, heappop

class Solution:
    def k_smallest_pairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        q = []
        res = []

        for i in range(min(k, len(nums1))):
            heappush(q, (nums1[i] + nums2[0], i, 0))
       
        while q and len(res) < k:
            _, i, j = heappop(q)
            res.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                heappush(q, (nums1[i] + nums2[j + 1], i, j + 1))
                
        return res

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(Solution().kSmallestPairs(nums1, nums2, k))