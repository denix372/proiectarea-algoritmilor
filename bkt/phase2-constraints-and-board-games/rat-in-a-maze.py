
# first solution of rat in a maze
def rat_in_maze(maze):
    n = len(maze)
    sol = [[0] * n for _ in range(n)]
    def back(x, y):
        if x == n - 1 and y == n - 1:
            sol[x][y] = 1
            return True
        
        if x < 0 or y < 0 or y >= n or x >= n:
            return False
        
        if maze[x][y] == 0 or sol[x][y] == 1:
            return False
        sol[x][y] = 1
            
        if back(x + 1, y):
            return True
        if back(x - 1, y):
            return True
        if back(x, y - 1):
            return True
        if back(x, y + 1):
            return True
        sol[x][y] = 0

    back(0, 0)
    return sol


# first solution of rat in a maze
def rat_in_maze_all(maze):
    n = len(maze)
    res = []
    sol = [[0] * n for _ in range(n)]

    def back(x, y, path):
        if x == n - 1 and y == n - 1:
            sol[x][y] = 1
            res.append(path)
            sol[x][y] = 0
            return
        
        if x < 0 or y < 0 or y >= n or x >= n:
            return 
        
        if maze[x][y] == 0 or sol[x][y] == 1:
            return 
        sol[x][y] = 1
            
        back(x + 1, y, path + 'D')
        back(x - 1, y, path + 'U')
        back(x, y - 1, path + 'L')
        back(x, y + 1, path + 'R')
        sol[x][y] = 0

    back(0, 0, "")
    return res


def rat_in_maze_all_matrixes(maze):

    n = len(maze)
    sol = [[0] * n for _ in range(n)]
    all_sol = []

    def back(x, y):
        if x == n - 1 and y == n - 1:
            sol[x][y] = 1

            snapshot = [row.copy() for row in sol]
            all_sol.append(snapshot)
            sol[x][y] = 0
            return
    
        if x < 0 or y < 0 or x >= n or y >= n:
            return
        
        if maze[x][y] == 0 or sol[x][y] == 1:
            return
        
        sol[x][y] = 1

        back(x + 1, y)
        back(x, y + 1)
        back(x - 1, y)
        back(x, y - 1)

        sol[x][y] = 0

    back(0, 0)
    return all_sol

maze = [
    [1, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 1]
]


print("------ If can be found a path ------")
paths = rat_in_maze(maze)
for p in paths:
    print(p)

print("------ All paths finding ------")

print(rat_in_maze_all(maze))


print("------ All paths in matrixes------")
solutions = rat_in_maze_all_matrixes(maze)

for idx, sol in enumerate(solutions):
    for row in sol:
        print(row)
    print()
