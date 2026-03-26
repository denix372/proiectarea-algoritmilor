
def solve(m):
    n = len(m)
    right = [[0] * n for _ in range(n)]
    down = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if m[i][j] == 'X':
                right[i][j] = 1 if j == n - 1 else right[i][j + 1] + 1
                down[i][j] = 1 if i == n - 1 else down[i + 1][j] + 1

    res = 0
    for i in range(n):
        for j in range(n):
            maxSide = min(right[i][j], down[i][j])
            for side in range(maxSide, 0, -1):
                if (right[i + side - 1][j] >= side and 
                    down[i][j + side - 1] >= side):
                    res = max(res, side)
                    break
    return res

mat = [ ['X', 'O', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'O', 'X', 'O'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'O', 'O'] ] 

print(solve(mat))