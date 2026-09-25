from typing import List

class Solution:
    def next_greater_element(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums2)
        res = {}
        stack = []

        for i, v in enumerate(nums2):
            while stack and stack[-1] < v:
                w = stack.pop()
                res[w] = v
            stack.append(v)

        n = len(nums1)
        res2 = [-1] * n
        for i in range(n):
            if nums1[i] in res:
                res2[i] = res[nums1[i]]
            else:
                res2[i] = -1
        return res2
        
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(Solution().nextGreaterElement(nums1, nums2))