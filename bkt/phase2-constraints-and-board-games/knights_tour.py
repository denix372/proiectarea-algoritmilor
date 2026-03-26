

def knight_tour(x, y, n):
    board = [[-1] * n for _ in range(n)]
    board[x][y] = 0
    moves = [[1, 2], [2, 1], [2, -1], [-1, 2],
             [-2, 1], [1, -2], [-1, -2], [-2, -1]]
    def back(x, y, cnt):
        if cnt ==  n * n:
            return True
        
        for (ox, oy) in moves:
            nx = x + ox
            ny = y + oy

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == -1:
                board[nx][ny] = cnt
                if back(nx, ny, cnt + 1):
                    return True
                board[nx][ny] = -1
        return False
    back(x, y, 1)
    return board

x, y, n = map(int, input().split())
res = knight_tour(x, y, n)
for r in res:
    for c in r:
        print(c, end = " " )
    print()