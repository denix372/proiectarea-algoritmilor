
def solve(heights):
    n = len(heights)
    res = []
    max_height = -1
    
    for i in range(n - 1, -1, -1):
        if heights[i] > max_height:
            res.append(i)
            max_height = heights[i]

    return res[::-1]

heights = [4,2,3,1]
print(solve(heights))