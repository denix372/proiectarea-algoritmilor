
class Solution:
    def countmerge(self, arr, left, mid, right):
            i, j, k = 0, 0, left
            n, m =  mid - left + 1 , right - mid
            v1 = arr[left : mid + 1]
            v2 = arr[mid + 1 : right + 1]

            inv = 0

            while i < n and j < m:
                if v1[i] <= v2[j]:
                    arr[k] = v1[i]
                    i += 1
                else:
                    arr[k] = v2[j]
                    j += 1
                    inv += (len(v1) - i)
                k += 1
            
            while i < n:
                arr[k] = v1[i]
                i += 1
                k += 1
            
            while j < m:
                arr[k] = v2[j]
                j += 1
                k += 1
            return inv

    def countInv(self, arr, left, right):
        res = 0

        if left < right:
            mid = (left + right) // 2
            res += self.countInv(arr, left, mid)
            res += self.countInv(arr, mid + 1, right)
            res += self.countmerge(arr, left, mid, right)
        return res

sol = Solution()
arr = [4, 3, 2, 1]
print(sol.countInv(arr, 0, len(arr) - 1))