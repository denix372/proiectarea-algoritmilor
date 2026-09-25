from typing import List, Optional
from collections import deque

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

def print_tree(root):
    if not root:
        print("[]")
        return

    res = []
    q = deque([root])

    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)

    while res and res[-1] is None:
        res.pop()

    print(res)

class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        lp = self.invertTree(root.left)
        rp = self.invertTree(root.right)
        root.right = lp
        root.left = rp
        return root

root = [4,2,7,1,3,6,9]
print_tree(Solution().invertTree(build_tree(root)))