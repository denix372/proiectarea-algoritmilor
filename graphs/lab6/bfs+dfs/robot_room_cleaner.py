
# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
class Robot:
    """
    A full simulation of the LeetCode robot.
    """

    # Directions: up, right, down, left
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self, room, start_row, start_col):
        self.room = room
        self.R = len(room)
        self.C = len(room[0])
        self.r = start_row
        self.c = start_col
        self.d = 0  # 0 = up
        self.cleaned = set()

    def move(self):
        dr, dc = Robot.DIRS[self.d]
        nr, nc = self.r + dr, self.c + dc
        if 0 <= nr < self.R and 0 <= nc < self.C and self.room[nr][nc] == 1:
            self.r, self.c = nr, nc
            return True
        return False

    def turnLeft(self):
        self.d = (self.d - 1) % 4

    def turnRight(self):
        self.d = (self.d + 1) % 4

    def clean(self):
        self.cleaned.add((self.r, self.c))

    def print_cleaned(self):
        print("Cleaned cells:", sorted(self.cleaned))


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def dfs(i, j, d):
            vis.add((i, j))
            robot.clean()
            for k in range(4):
                nd = (d + k) % 4
                x, y = i + dirs[nd], j + dirs[nd + 1]
                if (x, y) not in vis and robot.move():
                    dfs(x, y, nd)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnRight()

        dirs = (-1, 0, 1, 0, -1)
        vis = set()
        dfs(0, 0, 0)

if __name__ == "__main__":
    room = [
      [1,1,1,1,1,0,1,1],
      [1,1,1,1,1,0,1,1],
      [1,0,1,1,1,1,1,1],
      [0,0,0,1,0,0,0,0],
      [1,1,1,1,1,1,1,1]
    ]

    start_row = 1
    start_col = 3

    robot = Robot(room, start_row, start_col)
    sol = Solution()
    sol.cleanRoom(robot)

    robot.print_cleaned()
