def knights_tour(x, y, n):
    board = [[-1] * n for _ in range(n)]
    board[x][y] = 0
    
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    def back(x, y, cnt):
        if cnt == n * n:
            return True
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
                board[nx][ny] = cnt
                if back(nx, ny, cnt + 1):
                    return True
                board[nx][ny] = -1

        return False

    back(x, y, 1)
    return board

# exemplae for a 5 x 5 board
res = knights_tour(0, 0, 5)
for row in res:
    for val in row:
        print(val, end=" ")
    print()
