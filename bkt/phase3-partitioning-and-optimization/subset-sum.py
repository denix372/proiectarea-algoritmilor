from functools import lru_cache

class Solution:
    def isSubsetSum(self, arr: list[int], sum: int) -> bool:
        # code here
        n = len(arr)

        # for optimization decomment this
        # @lru_cache(None)
        def back(n, target):
            if target == 0:
                return True
            if n == 0:
                return False
            
            if arr[n - 1] > target:
                return back(n - 1, target)

            return back(n - 1, target) or back(n - 1, target - arr[n - 1])
        
        return back(n, sum)

arr = [3, 34, 4, 12, 5, 2]
sum = 9
sol = Solution()
print(sol.isSubsetSum(arr, sum))