from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr):
    if not arr or arr[0] is None:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in arr]

    i = 0
    child = 1
    while child < len(arr):
        if nodes[i] is not None:
            if child < len(arr):
                nodes[i].left = nodes[child]
            child += 1

            if child < len(arr):
                nodes[i].right = nodes[child]
            child += 1
        i += 1

    return nodes[0]

def find_node (root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def add_parents(node, parent):
            if node:
                node.parent = parent
                add_parents(node.left, node)
                add_parents(node.right, node)
                
        add_parents(root, None)
        
        queue = deque([(target, 0)])
        visited = set([target])
        
        while queue:
            u, dist = queue.popleft()
            
            if dist == k:
                return [u.val] + [n.val for n, d in queue]
                
            for v in (u.left, u.right, u.parent):
                if v and v not in visited:
                    visited.add(v)
                    queue.append((v, dist + 1))
   
        return []

root = build_tree([3,5,1,6,2,0,8,None,None,7,4])
target = find_node(root, 5)
k = 2
print(Solution().distanceK(root, target, k))