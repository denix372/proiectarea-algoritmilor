from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

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

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        res = []
        def dfs(node, sol):
            if not node:
                return

            if (node
                and not node.right
                and not node.left):
                    sol = sol + str(node.val)
                    res.append(sol)
                    return
    
            dfs(node.left, sol + str(node.val) + "->")
            dfs(node.right, sol + str(node.val) + "->")

        dfs(root, "")
        return res

root = [1,2,3,None,5]
print(Solution().binaryTreePaths(build_tree(root)))