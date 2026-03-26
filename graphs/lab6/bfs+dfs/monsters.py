import sys
from collections import deque

def solve():
    # Read all inputs at once (much faster for large grid problems)
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    matrix = input_data[2:]

    # Distances for monsters and A
    INF = float('inf')
    monster_dist = [[INF] * m for _ in range(n)]
    A_dist = [[INF] * m for _ in range(n)]

    # To reconstruct the path without memory limit errors
    parent = [[None] * m for _ in range(n)]

    q_m = deque()
    start_A = None

    # Find all Monsters and the start position A
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'M':
                monster_dist[i][j] = 0
                q_m.append((i, j))
            elif matrix[i][j] == 'A':
                start_A = (i, j)
                A_dist[i][j] = 0

    dirs = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]

    # 1. Multi-source BFS for all monsters simultaneously
    # This finds the absolute minimum time for *any* monster to reach any cell
    while q_m:
        r, c = q_m.popleft()
        for dr, dc, _ in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] != '#':
                if monster_dist[nr][nc] == INF:
                    monster_dist[nr][nc] = monster_dist[r][c] + 1
                    q_m.append((nr, nc))

    # 2. BFS for A
    q_a = deque([start_A])
    end_A = None

    while q_a:
        r, c = q_a.popleft()

        # Check if we hit the boundary
        if r == 0 or r == n - 1 or c == 0 or c == m - 1:
            end_A = (r, c)
            break

        for dr, dc, d_char in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] != '#':
                # Valid move ONLY if A can get there strictly faster than ANY monster
                if A_dist[r][c] + 1 < monster_dist[nr][nc] and A_dist[nr][nc] == INF:
                    A_dist[nr][nc] = A_dist[r][c] + 1
                    parent[nr][nc] = (r, c, d_char)
                    q_a.append((nr, nc))

    # 3. Path reconstruction
    if end_A:
        print("YES")
        path = []
        curr = end_A

        while curr != start_A:
            r, c = curr
            pr, pc, d_char = parent[r][c]
            path.append(d_char)
            curr = (pr, pc)

        path.reverse()
        print(len(path))
        print("".join(path))
    else:
        print("NO")

if __name__ == '__main__':
    solve()