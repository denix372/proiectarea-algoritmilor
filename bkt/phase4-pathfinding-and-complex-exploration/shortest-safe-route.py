# backtracking approach
def shortest_safe_route(mat):
    n = len(mat)
    m = len(mat[0])
    best = [float('inf')]
    mat2 = [row[:] for row in mat]
    visited = [[False] * m for _ in range(n)]

    # mark all adjacent cells with landmines with 0 
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                if i + 1 < n:
                    mat2[i + 1][j] = 0
                if i - 1 >= 0:
                    mat2[i - 1][j] = 0
                if j + 1 < m:
                    mat2[i][j + 1] = 0
                if j - 1 >= 0:
                    mat2[i][j - 1] = 0

    def back(x, y,steps):
        if y == m - 1:
            best[0] = min(best[0], steps)
            return

        if x < 0 or y < 0 or x >= n or y >= m:
            return
        
        if visited[x][y] or mat2[x][y] == 0:
            return

        visited[x][y] = True
        back(x + 1, y, steps + 1)
        back(x, y + 1, steps + 1)
        back(x - 1, y, steps + 1)
        back(x, y - 1, steps + 1)
        visited[x][y] = False
        return

    for i in range(n):
            back(i, 0, 1)

    if (best[0] == float('inf')):
        return -1
    return best[0]


#BFS 
from collections import deque

def isSafe(mat, i, j):
    r, c = len(mat), len(mat[0])

    # celula trebuie să fie 1 (sigură)
    if mat[i][j] != 1:
        return False

    # nu trebuie să fie lângă o mină
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        ni, nj = i + dx, j + dy
        if 0 <= ni < r and 0 <= nj < c and mat[ni][nj] == 0:
            return False

    return True


def shortest_safe_route2(mat):
    r, c = len(mat), len(mat[0])
    q = deque()

    # 1. add all the alone cells from the first column
    for i in range(r):
        if isSafe(mat, i, 0):
            q.append((i, 0, 1))   # (x, y, dist)
            mat[i][0] = -1        # mark as visited

    # 2. BFS
    while q:
        x, y, dist = q.popleft()

        if y == c - 1:
            return dist

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and isSafe(mat, nx, ny):
                q.append((nx, ny, dist + 1))
                mat[nx][ny] = -1  #mark as visited

    return -1

    
mat = [ [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0] ]

print(shortest_safe_route(mat))