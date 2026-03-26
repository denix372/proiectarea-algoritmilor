class Solution:
    def merge(self, arr, left, mid, right):
            i, j, k = 0, 0, left
            n, m =  mid - left + 1 , right - mid
            v1 = arr[left : mid + 1]
            v2 = arr[mid + 1 : right + 1]

            while i < n and j < m:
                if v1[i] < v2[j]:
                    arr[k] = v1[i]
                    i += 1
                else:
                    arr[k] = v2[j]
                    j += 1
                k += 1
            
            while i < n:
                arr[k] = v1[i]
                i += 1
                k += 1
            
            while j < m:
                arr[k] = v2[j]
                j += 1
                k += 1

    def mergeSort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            self.mergeSort(arr, left, mid)
            self.mergeSort(arr, mid + 1, right)
            self.merge(arr, left, mid, right)

sol = Solution()
arr = [4, 1, 3, 8, 7]
sol.mergeSort(arr, 0, len(arr) - 1)
print(arr)