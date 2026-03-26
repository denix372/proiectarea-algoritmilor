from collections import deque
 
def labyrinth(n, m, a, source, destination):
    visited =[[False] * m for _ in range(n)]
    p = [[None] * m for _ in range(n)]
    q = deque()
 
    q.append(source)
    visited[source[0]][source[1]]

    moves = [(0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L'), (-1, 0, 'U')]
 
    while q:
        x, y = q.popleft()
 
        if (x, y) == destination:
            path = []
            cx, cy = destination
            while (cx, cy) != source:
                px, py, mv = p[cx][cy]
                path.append(mv)
                cx, cy = px, py
            path.reverse()
            return 'YES', len(path), "".join(path)
 
        for dx, dy, move in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and a[nx][ny] != '#':
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    p[nx][ny] = (x, y, move)
 
    return 'NO', None, None
 
#second code is an optimization to pass all tests on cses
def labyrinth2(n, m, a, source, destination):
    visited =[[False] * m for _ in range(n)]
    px = [[-1] * m for _ in range(n)]
    py = [[-1] * m for _ in range(n)]
    pm = [[''] * m for _ in range(n)]
    q = deque()
 
    q.append(source)
    visited[source[0]][source[1]] = True
    l = 0
 
    moves = [(0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L'), (-1, 0, 'U')]
 
    while q:
        x, y = q.popleft()
 
        if (x, y) == destination:
            path = []
            cx, cy = destination
            while (cx, cy) != source:
                mv = pm[cx][cy]
                path.append(mv)
                nx = px[cx][cy]
                ny = py[cx][cy]
                cx, cy = nx, ny
            path.reverse()
            return 'YES', len(path), "".join(path)
 
        for dx, dy, move in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and a[nx][ny] != '#':
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    px[nx][ny] = x
                    py[nx][ny] = y
                    pm[nx][ny] = move
 
    return 'NO', None, None

n, m = map(int, input().split())
a =[]
for i in range(n):
    line = input().strip()
    a.append(line)
    for j in range(m):
        if a[i][j] == 'A':
            source = (i, j)
        if a[i][j] == 'B':
            dest = (i, j)
res, l, p = labyrinth2(n, m, a, source, dest)
if res == "NO":
    print("NO")
else:
    print("YES")
    print(l)
    print(p)
