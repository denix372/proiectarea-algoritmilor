class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
            i = self.partition(arr, low, high)
            self.quickSort(arr, low, i - 1)
            self.quickSort(arr, i + 1, high)

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
sol.quickSort(arr, 0, len(arr) - 1)
print(arr)