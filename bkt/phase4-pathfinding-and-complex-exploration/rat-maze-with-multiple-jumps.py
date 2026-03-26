
# first solution of rat in a maze
def rat_in_maze_with_multiple_jumps(maze):
    n = len(maze)
    sol = [[0] * n for _ in range(n)]
    
    def back(x, y, steps):
        if x == n - 1 and y == n - 1:
            sol[x][y] = 1
            return True
            
        if x < 0 or y < 0 or y >= n or x >= n or maze[x][y] == 0:
            return False
            
        sol[x][y] = 1
        
        for i in range(1, maze[x][y] + 1):
            if y + i < n and back(x, y + i, steps + 1):
                return True
            if x + i < n and back(x + i, y, steps + 1):
                return True
        
        sol[x][y] = 0
        return False

    if back(0, 0, 0):
        return sol
    else:
        return [[-1]]



maze = [
    [2, 1, 0, 0],
    [3, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 1]
]

paths = rat_in_maze_with_multiple_jumps(maze)
for p in paths:
    print(p)