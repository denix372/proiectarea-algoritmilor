class Solution:
    def quickSelect(self, arr, low, high, k):
        if low <= high:
            pivot = self.partition(arr, low, high)

            if pivot == k:
                return arr[pivot]
            elif pivot > k:
                return self.quickSelect(arr, low, pivot -1, k)
            else:
                return self.quickSelect(arr, pivot + 1,high, k)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

sol = Solution()
arr = [4, 1, 3, 8, 7]
k = 3  #(0-based searching)
print(sol.quickSelect(arr, 0, len(arr) - 1, k))