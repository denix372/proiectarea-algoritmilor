import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# regular approach, but gives TLE
def counting_rooms(n, m, a):
    
    visited = [[False] * m for _ in range(n)]
    def dfs(x, y):
        if visited[x][y] == True:
            return 0
        visited[x][y] = True
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] != '#':
                    dfs(nx, ny)
        return 1
    s = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] != '#':
                s += dfs(i, j)
    return s


# same approach but with stack insteas of recursion
def counting_rooms2(n, m, a):
    
    visited = [[False] * m for _ in range(n)]
    
    def dfs(sx, sy):
        if visited[sx][sy] == True:
            return 0
        
        stack = [(sx, sy)]
        visited[sx][sy] = True
        while stack:
            x, y = stack.pop()
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] != '#' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
        return 1
    s = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] != '#':
                s += dfs(i, j)
    return s



# same approach but with queue
def counting_rooms3(n, m, a):
    visited = [[False] * m for _ in range(n)]
    
    def bfs(sx, sy):
        q = deque([(sx, sy)])
        visited[sx][sy] = True
        while q:
            x, y = q.popleft()
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and a[nx][ny] == '.':
                        visited[nx][ny] = True
                        q.append((nx, ny))
        return 1
    s = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == '.' and not visited[i][j]:
                bfs(i, j)
                s += 1
    return s

def main():
    n, m = map(int, input().split())
    a = [list(input().strip()) for _ in range(n)]
    print(counting_rooms3(n, m, a))

if __name__ == "__main__":
    main()