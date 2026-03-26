

def solve(colors):
    n = len(colors)

    red = [0] * (n + 1)
    blue = [0] * (n + 1)
    green = [0] * (n + 1)
    red[0] = colors[0][0]
    blue[0] = colors[0][1]
    green[0] = colors[0][2]
    for i in range(1, n):
        r, b, g = colors[i]
        red[i] = r + min(blue[i - 1], green[i - 1])
        blue[i] = b + min(red[i - 1], green[i - 1])
        green[i] = g + min(blue[i - 1], red[i - 1])

    return min(red[n - 1], green[n - 1], blue[n - 1])

colors = [[17,2,17],[16,16,5],[14,3,19]]
print(solve(colors))
                                