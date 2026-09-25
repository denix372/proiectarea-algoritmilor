from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def build_graph(adjList):
    if not adjList:
        return None
    
    nodes = {i+1: Node(i+1) for i in range(len(adjList))}
    
    for i, neighbors in enumerate(adjList):
        for nb in neighbors:
            nodes[i+1].neighbors.append(nodes[nb])
    
    return nodes[1]

def print_graph(node):
    visited = set()
    res = []
    def dfs(u):
        if u.val in visited:
            return
        visited.add(u.val)
        res.append([v.val for v in u.neighbors])
        for v in u.neighbors:
            dfs(v)
    dfs(node)
    print(res)

class Solution:
    def clone_graph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        cloned = {}

        def dfs(u):
            if u in cloned:
                return cloned[u]

            clone = Node(u.val)
            cloned[u] = clone

            for v in u.neighbors:
                clone.neighbors.append(dfs(v))
            
            return clone

        return dfs(node)

adjList = [[2,4],[1,3],[2,4],[1,3]]
print_graph(Solution().cloneGraph(build_graph(adjList)))