#decomment just if you use the first function
#import sys
#sys.setrecursionlimit(300000)

from collections import deque

def findOrder(numCourses, prerequisites):
    prereq = {c : [] for c in range(1, numCourses + 1)}
    for c, p in prerequisites:
        prereq[c].append(p)

    output = []
    visit, cycle = set(), set()
    def dfs(crs):
        if crs in cycle:
            return False
        if crs in visit:
            return True

        cycle.add(crs)
        for pre in prereq[crs]:
            if dfs(pre) == False:
                return False
        cycle.remove(crs)
        visit.add(crs)
        output.append(crs)
    
    for c in range(1, numCourses + 1):
        if dfs(c) == False:
            return []
    
    output.reverse()
    return output


def dfs_stack(numCourses, prerequisites):
    prereq = {c : [] for c in range(1, numCourses + 1)}
    for c, p in prerequisites:
        prereq[c].append(p)

    output = []
    visit, cycle = set(), set()
    def dfs(start):
        stack = [(start, 0)]

        while stack:
            node, idx = stack.pop()
            if node in cycle and idx == 0:
                return False
            if node in visit:
                return True

            if idx == 0:
                cycle.add(node)

            if idx == len(prereq[node]):
                cycle.discard(node)
                visit.add(node)
                output.append(node)
                continue

            stack.append((node, idx + 1))
            nxt = prereq[node][idx]

            if nxt in cycle:
                return False
            if nxt not in visit:
                stack.append((nxt, 0))
        return True
    
    for c in range(1, numCourses + 1):
        if c not in visit:
            if not dfs(c):
                return []
    
    output.reverse()
    return output


def bfs_khan(n, prerequisites):
    adj = {c : [] for c in range(1, n + 1)}
    indeg = {c : 0 for c in range(1, n + 1)}

    for a, b in prerequisites:
        adj[a].append(b)
        indeg[b] += 1

n, m = map(int, input().split())
req = []

for _ in range(m):
    (a, b) = map(int, input().split())
    req.append([a, b])

res = dfs_stack(n, req)
if res == []:
    print("IMPOSSIBLE")
else:
    for i in res:
        print(i, end = " ")