from collections import deque

INF = 10**9
class Solution:
    def minThrows(self, n, lad, sn):
        # code here
        adj = [[] for _ in range(n * n + 1)]
    
        for i in range(0, len(lad), 2):
            a, b = lad[i], lad[i + 1]
            adj[a].append(b)

        for i in range(0, len(sn), 2):
            a, b = sn[i], sn[i + 1]
            adj[a].append(b)

        q = deque([1])
        dist = [INF] * (n * n + 1)
        dist[1] = 0
        while q:
            u = q.popleft()
            for v in range(u + 1, min(u + 7, n * n + 1)):
                
                # Check if this cell is the start of a snake or ladder
                # If adj[v] is not empty, our destination changes to adj[v][0]
                dest = v
                if adj[v]:
                    dest = adj[v][0]
                
                # Only update distance and append if the final destination is unvisited
                if dist[dest] == INF:
                    dist[dest] = dist[u] + 1
                    q.append(dest)
            
    
        if dist[n * n] == INF:
            return -1
        return dist[n * n]


# approach with a dict
class Solution2:
    def minThrows(self, n, lad, sn):
        target = n * n
        
        board = {}
        for i in range(0, len(lad), 2):
            board[lad[i]] = lad[i + 1]
            
        for i in range(0, len(sn), 2):
            board[sn[i]] = sn[i + 1]

        dist = [-1] * (target + 1)
        dist[1] = 0
        q = deque([1])
        
        while q:
            u = q.popleft()
            
            if u == target:
                return dist[u]
                
            # Roll the dice: 1 through 6
            for dice in range(1, 7):
                v = u + dice

                if v <= target:
                    # If there's a snake or ladder, take it immediately
                    v = board.get(v, v)
                    
                    # If this final destination hasn't been visited yet
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        q.append(v)
        
        return -1

n = 6
lad = [3, 22, 5, 8, 11, 35, 20, 32]
sn = [17, 4, 19, 7, 34, 1, 21, 9]

print(Solution().minThrows(n, lad, sn))
print(Solution2().minThrows(n, lad, sn))