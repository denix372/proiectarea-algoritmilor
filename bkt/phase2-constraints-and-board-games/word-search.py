from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        res = []
        visited = [[False] * m for _ in range(n)]

        def back(x, y, index):
            if index == len(word):
                return True

            if x < 0 or y < 0 or x >= n or y >= m:
                return False

            if visited[x][y] or word[index] != board[x][y]:
                return False

            visited[x][y] = True
            if back(x + 1, y, index + 1):
                return True
            if back(x - 1, y, index + 1):
                return True
            if back(x, y + 1, index + 1):
                return True
            if back(x, y - 1, index + 1):
                return True
            visited[x][y] = False
            return False

        for i in range(n):
            for j in range(m):
                if back(i, j, 0):
                    return True

        return False

if __name__ == "__main__":
    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ]
    word = "ABCCED"

    sol = Solution()
    print(sol.exist(board, word))   # True