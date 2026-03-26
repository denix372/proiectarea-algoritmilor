from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n

        def dfs(u):
            visited[u] = True
            for v in rooms[u]:
                if not visited[v]:
                    dfs(v)

        dfs(0)
        return all(visited)
sol = Solution()
rooms = [[1,3],[3,0,1],[2],[0]]
print(sol.canVisitAllRooms(rooms))