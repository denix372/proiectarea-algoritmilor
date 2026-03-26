# Python program to implement
# box stacking problem

def maxHeight(height, width, length):
    n = len(height)
    boxes = []
    for i in range(n):
        a, b, c = height[i], width[i], length[i]
        boxes.append([a, b, c])
        boxes.append([a, c, b])
        boxes.append([b, a, c])
        boxes.append([b, c, a])
        boxes.append([c, a, b])
        boxes.append([c, b, a])
    
    # Sort the boxes in descending 
    # order of length and width.
    boxes.sort(key=lambda x: (x[0], x[1]), reverse=True)
    
    dp = [0] * len(boxes)
    ans = 0
    
    for i in range(len(boxes) - 1, -1, -1):
        dp[i] = boxes[i][2]
        for j in range(i + 1, len(boxes)):
            if boxes[i][0] > boxes[j][0] and boxes[i][1] > boxes[j][1]:
                dp[i] = max(dp[i], boxes[i][2] + dp[j])

        ans = max(ans, dp[i])
    
    return ans

if __name__ == "__main__":
    height = [4, 1, 4, 10]
    width = [6, 2, 5, 12]
    length = [7, 3, 6, 32]
    
    print(maxHeight(height, width, length))