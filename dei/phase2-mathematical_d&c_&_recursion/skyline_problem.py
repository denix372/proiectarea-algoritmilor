from typing import List
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        def divide(b, l, r):
            if l == r:
                L, R, H = b[l]
                return [[L, H], [R, 0]]

            mid = (l + r) // 2
            left = divide(b, l, mid)
            right = divide(b, mid + 1, r)
            return merge(left, right)

        def merge(A, B):
            i = j = h1 = h2 = 0
            res = []

            while i < len(A) and j < len(B):
                if A[i][0] < B[j][0]:
                    x, h1 = A[i]
                    i += 1
                elif B[j][0] < A[i][0]:
                    x, h2 = B[j]
                    j += 1
                else:
                    x = A[i][0]
                    h1 = A[i][1]
                    h2 = B[j][1]
                    i += 1
                    j += 1
                
                cur = max(h1, h2)
                if not res or res[-1][1] != cur:
                    res.append([x, cur])
                
            res.extend(A[i:])
            res.extend(B[j:])

            final = []
            for x, h in res:
                if not final or final[-1][1] != h:
                    final.append([x, h])

            return final
            
        return divide(buildings, 0, len(buildings) - 1)

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print(Solution().getSkyline(buildings))