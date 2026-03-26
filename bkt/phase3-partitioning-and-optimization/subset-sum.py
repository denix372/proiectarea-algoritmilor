class Solution:
    def isSubsetSum(self, N, arr, sum):
        
        def back(n, target):
            if target == 0:
                return True
            if n == 0:
                return False
            
            if arr[n - 1] > target:
                return back(n - 1, target)
            
            return back(n - 1, target) or back(n - 1, target - arr[n - 1])
        
        return back(N, sum)


arr = [3, 34, 4, 12, 5, 2]
sum = 9
sol = Solution()
print(sol.isSubsetSum(len(arr), arr, sum))