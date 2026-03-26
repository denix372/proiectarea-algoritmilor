import sys
from collections import deque

def labyrinth(start, end, grid, n, m):
    visited = [[False] * m for _ in range(n)]
    dist = [[0] * m for _ in range(n)]
    parent = [[None] * m for _ in range(n)]
    q = deque()

    si, sj = start
    visited[si][sj] = True
    q.append((si, sj))

    dirs = [(1, 0, 'D'), (0, 1, 'R'), (-1, 0, 'U'), (0, -1, 'L')]

    while q:
        i, j = q.popleft()

        if (i, j) == end:
            return dist[i][j], parent

        for di, dj, move in dirs:
            ni, nj = i + di, j + dj

            if 0 <= ni < n and 0 <= nj < m:
                if not visited[ni][nj] and grid[ni][nj] != '#':
                    visited[ni][nj] = True
                    dist[ni][nj] = dist[i][j] + 1
                    parent[ni][nj] = (i, j, move)
                    q.append((ni, nj))

    return -1, parent


def reconstruct_path(parent, start, end):
    path = []
    i, j = end

    while (i, j) != start:
        pi, pj, move = parent[i][j]
        path.append(move)
        i, j = pi, pj

    return "".join(reversed(path))


def main():
    data = sys.stdin
    n, m = map(int, data.readline().split())
    grid = [list(data.readline().strip()) for _ in range(n)]

    start = end = None

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'A':
                start = (i, j)
            elif grid[i][j] == 'B':
                end = (i, j)

    length, parent = labyrinth(start, end, grid, n, m)

    if length == -1:
        print("NO")
    else:
        print("YES")
        print(length)
        print(reconstruct_path(parent, start, end))


if __name__ == "__main__":
    main()
