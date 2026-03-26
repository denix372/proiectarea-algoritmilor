from typing import List
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        # arr.sort() # but is already sorted

        n = len(arr)
        if arr[0] != 0:
            return 0
        if arr[n - 1] != n:
            return n

        lo, hi = 0, n - 1
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if arr[lo] - lo != arr[mid] - mid:
                hi = mid
            elif arr[hi] - hi != arr[mid] - mid:
                lo = mid
        return arr[lo] + 1

nums = [0, 1, 3]
print(Solution().missingNumber(nums))