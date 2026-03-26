
class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        s = 0
        for i in range(k):
            s += arr[i]
    
        max_sum = s
        for i in range(k, len(arr)):
            s += arr[i] - arr[i - k]
            max_sum = max(max_sum, s)
        
        return max_sum

arr = [100, 200, 300, 400]
k = 2
print(Solution().maxSubarraySum(arr, k))