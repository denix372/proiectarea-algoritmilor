def knights_tour(x, y, n):
    board = [[-1] * n for _ in range(n)]
    board[x][y] = 1
    
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    def degree(x, y):
        cnt = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
                cnt += 1
        return cnt

    def back(x, y, cnt):
        if cnt == n * n + 1:
            return True
        
        moves = []
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
                moves.append((degree(nx, ny), nx, ny))
        
        moves.sort(key=lambda t: t[0])
        
        for _, nx, ny in moves:
            board[nx][ny] = cnt
            if back(nx, ny, cnt + 1):
                return True
            board[nx][ny] = -1

        return False

    back(x, y, 2)
    return board

# exemplee for a 8 x  board
y, x = map(int, input().split())
res = knights_tour(x - 1, y - 1, 8)
for row in res:
    for val in row:
        print(val, end=" ")
    print()
