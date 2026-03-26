from typing import List
from collections import deque

INF = 10**3
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(watchedVideos)
        q = deque([id])
        dist = [INF] * n
        dist[id] = 0
        freq = {}

        while q:
            u = q.popleft()

            if dist[u] == level:
                for r in watchedVideos[u]:
                    if r not in freq:
                        freq[r] = 1
                    else:
                        freq[r] += 1

            for v in friends[u]:
                if dist[v] == INF:
                    dist[v] = dist[u] + 1
                    q.append(v)
        
        videos = list(freq.items())
        videos.sort(key = lambda x : (x[1], x[0]))
        return [x[0] for x in videos]

watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
id = 0
level = 1
print(Solution().watchedVideosByFriends(watchedVideos, friends, id, level))