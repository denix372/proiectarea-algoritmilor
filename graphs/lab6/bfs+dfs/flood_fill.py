from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        visited = [[False] * m for _ in range(n)]
        queue = []

        original  = image[sr][sc]
        if original == color:
            return image

        visited[sr][sc] = True
        queue.append((sr,sc))
        image[sr][sc] = color

        while queue:
            pi, pj = queue.pop(0)
    
            for oi, oj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni = pi + oi
                nj = pj + oj

                if 0 <= ni < n and 0 <= nj < m:
                    if image[ni][nj] == original and not visited[ni][nj]:
                        image[ni][nj] = color
                        visited[ni][nj] = True
                        queue.append((ni, nj))
            
        return image
        

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
sol = Solution()
new_image = sol.floodFill(image, sr, sc, color)
for r in new_image:
    print(r)