from typing import List

INF = 10**4 + 1
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        nodel = [-INF] * n
        onedel = [-INF] * n
        nodel[0] = arr[0]

        for i in range(1, n):
            nodel[i] = max(nodel[i - 1] + arr[i], arr[i])
            onedel[i] = max(onedel[i - 1] + arr[i], nodel[i - 1])

        return max(max(nodel), max(onedel))

arr = [1,-2,0,3]
print(Solution().maximumSum(arr))