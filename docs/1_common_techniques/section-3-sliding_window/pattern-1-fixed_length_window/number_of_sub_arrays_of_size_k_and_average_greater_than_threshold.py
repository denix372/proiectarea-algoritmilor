
class Solution:
    def num_of_subarrays(self, arr: list[int], k: int, threshold: int) -> int:
        s = 0
        for i in range(k):
            s += arr[i]
        avg = s / k
        cnt = 0
        if avg >= threshold:
            cnt += 1
    
        for i in range(k, len(arr)):
            s += arr[i] - arr[i - k]
            avg = s / k
            if avg >= threshold:
                cnt += 1
        
        return cnt

arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
print(Solution().numOfSubarrays(arr, k, threshold))