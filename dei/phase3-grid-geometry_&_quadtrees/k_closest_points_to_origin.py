from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(p):
            return p[0]*p[0] + p[1]*p[1]

        def select(left, right, k):
            pivot = dist(points[(left+right)//2])
            i, j = left, right

            while i <= j:
                while dist(points[i]) < pivot:
                    i += 1
                while dist(points[j]) > pivot:
                    j -= 1
                if i <= j:
                    points[i], points[j] = points[j], points[i]
                    i += 1
                    j -= 1

            if left + k - 1 <= j:
                return select(left, j, k)
            if left + k - 1 >= i:
                return select(i, right, k - (i - left))
            return

        select(0, len(points)-1, k)
        return points[:k]

points = [[3,3],[5,-1],[-2,4]]
k = 2
print(Solution().kClosest(points, k))