from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    b = (r // 3) * 3 + c // 3
                    self.rows[r].add(board[r][c] )
                    self.cols[c].add(board[r][c] )
                    self.boxes[b].add(board[r][c])
        def back():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for k in "123456789":
                            b = (r // 3) * 3 + c // 3
                            if (k not in self.rows[r]
                                and k not in self.cols[c]
                                and k not in self.boxes[b]):

                                board[r][c] = k
                                self.rows[r].add(k)
                                self.cols[c].add(k)
                                self.boxes[b].add(k)

                                back()
                                
                                board[r][c] = "."
                                self.rows[r].remove(k)
                                self.cols[c].remove(k)
                                self.boxes[b].remove(k)
                        return            
            for row in board:
                print(" ".join(row))
            print()
            return

        back()

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","."],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".",".","1","9",".",".","5"],
         [".",".",".",".","8",".",".",".","."]]
Solution().solveSudoku(board)