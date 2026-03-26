from typing import List
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        m, n = len(A), len(B)

        if m > n:
            A, B, m, n = B, A, n, m

        imin, imax = 0, m
        half = (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half - i

            if i < m and j > 0 and B[j-1] > A[i]:
                imin = i + 1
            elif i > 0 and j < n and A[i-1] > B[j]:
                imax = i - 1
            else:
                if i == 0:
                    max_left = B[j-1]
                elif j == 0:
                    max_left = A[i-1]
                else:
                    max_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return float(max_left)

                if i == m:
                    min_right = B[j]
                elif j == n:
                    min_right = A[i]
                else:
                    min_right = min(A[i], B[j])

                return (max_left + min_right) / 2.0

nums1 = [1,3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))