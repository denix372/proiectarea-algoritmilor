from collections import deque

def path(matrix):
    n = len(matrix)
    m = len(matrix[0])

    def feasible(mid):
        if matrix[0][0] < mid:
            return False
        
        visited = [[False] * m for _ in range(n)]
        q = deque([(0, 0)])
        visited[0][0] = True
        while q:
            x, y = q.popleft()
            if x == n - 1 and y == m - 1:
                return True

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if matrix[nx][ny] >= mid:
                        q.append((nx, ny))
        return False

    left = 1
    right = max([max(l) for l in matrix])

    while left <= right:
        mid = (left + right) // 2

        if feasible(mid):
            left = mid + 1
        else:
            right = mid - 1
    return right

matrix =  [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
print(path(matrix))