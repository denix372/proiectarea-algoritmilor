
class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr1.sort()
        arr2.sort()

        cnt = 0
        j = 0

        for i in range(len(arr1)):
            while j < len(arr2) and arr2[j] < arr1[i] - d:
                j += 1
            
            if j < len(arr2) and arr2[j] <= arr1[i] + d:
                continue
            else:
                cnt += 1
        return cnt

arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
print(Solution().findTheDistanceValue(arr1, arr2, d))