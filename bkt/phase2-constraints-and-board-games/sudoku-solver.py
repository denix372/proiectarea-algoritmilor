from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    self.rows[r].add(board[r][c])
                    self.cols[c].add(board[r][c])
                    b = (r//3 ) * 3 + (c //3 )
                    self.boxes[b].add(board[r][c])

        def backtrack(board):
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for num in "123456789":
                            b = (r // 3 ) * 3 + (c // 3)

                            if (num not in self.rows[r]
                            and num not in self.cols[c]
                            and num not in self.boxes[b]):

                                board[r][c] = num
                                self.rows[r].add(num)
                                self.cols[c].add(num)
                                self.boxes[b].add(num)

                                if backtrack(board):
                                    return True

                                board[r][c] = '.'
                                self.rows[r].remove(num)
                                self.cols[c].remove(num)
                                self.boxes[b].remove(num)


                        return False
            return True
        backtrack(board)



board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

sol = Solution()
sol.solveSudoku(board)
for row in board:
    print(row)