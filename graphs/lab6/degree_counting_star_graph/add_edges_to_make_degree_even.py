from typing import List

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n + 1)]
        degre = [0] * (n + 1)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            degre[a] += 1
            degre[b] += 1
        
        cnt = 0
        pos = []
        for i in range(1, n + 1):
            if degre[i] % 2 == 1:
                cnt += 1
                pos.append(i)

        if cnt == 0:
            return True    
        if cnt % 2 == 1 or cnt >= 5:
            return False

        # only 2 possibilities 2, 4
        actual = set([(min(a, b), max(a, b)) for a, b in edges])

        if len(pos) == 2:
            a = pos[0]
            b = pos[1]

            # Option 1: Connect a and b directly
            if (a, b) not in actual:
                return True

            # Option 2: Connect both a and b to an intermediate even node
            for i in range(1, n + 1):
                if i != a and i != b:
                    if (not (min(a, i), max(a, i)) in actual and
                        not (min(b,i), max(b, i)) in actual):
                        return True
            return False
        
        if len(pos) == 4:
            a = pos[0]
            b = pos[1]
            c = pos[2]
            d = pos[3]
            # only 4 nodes can be right
            # a, b and c, d
            # a, c and b , d
            # a d and c, b

            if (a, b) not in actual and (c, d) not in actual:
                return True
            if (a, c) not in actual and (b, d) not in actual:
                return True
            if (a, d) not in actual and (b, c) not in actual:
                return True

        return False

n = 5
edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
print(Solution().isPossible(n, edges))