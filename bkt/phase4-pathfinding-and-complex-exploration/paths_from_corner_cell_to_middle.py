
def solve(mat):
    n = len(mat)
    mid = n // 2
    res = []
    visited = [[False] * n for _ in range(n)]

    def back(i, j, sol):
        if i == mid and j == mid:
            res.append(sol.copy())
            return

        if i < 0 or j < 0 or i >= n or j >= n:
            return
        if visited[i][j]:
            return


        k = mat[i][j]
        visited[i][j] = True

        back(i + k, j, sol + [(i + k, j)])
        back(i - k, j, sol + [(i - k, j)])
        back(i, j + k, sol + [(i, j + k)])
        back(i, j - k, sol + [(i, j - k)])

        visited[i][j] = False

    back(0, 0, [(0, 0)])
    return res

mat = [ [ 3, 5, 4, 4, 7, 3, 4, 6, 3 ],
        [ 6, 7, 5, 6, 6, 2, 6, 6, 2 ],
        [ 3, 3, 4, 3, 2, 5, 4, 7, 2 ],
        [ 6, 5, 5, 1, 2, 3, 6, 5, 6 ],
        [ 3, 3, 4, 3, 0, 1, 4, 3, 4 ],
        [ 3, 5, 4, 3, 2, 2, 3, 3, 5 ],
        [ 3, 5, 4, 3, 2, 6, 4, 4, 3 ],
        [ 3, 5, 1, 3, 7, 5, 3, 6, 4 ],
        [ 6, 2, 4, 3, 4, 5, 4, 5, 1 ] ]
print(*solve(mat))










