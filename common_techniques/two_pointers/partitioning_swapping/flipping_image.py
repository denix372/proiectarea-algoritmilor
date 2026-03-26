
class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        m = len(image[0]) - 1
        for v in image:
            i, j = 0, m
            while i <= j:
                v[i], v[j] = 1 - v[j], 1 - v[i]
                i += 1
                j -= 1
        
        return image
            

image = [[1,1,0],[1,0,1],[0,0,0]]
print(Solution().flipAndInvertImage(image))