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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, n):
            if not node:
                return 0

            if not node.left and not node.right:
                return n * 10 + node.val

            return (dfs(node.left, n * 10 + node.val)
                    + dfs(node.right, n * 10 + node.val))

        return dfs(root, 0)

root = [1,2,3]
print(Solution().sumNumbers(build_tree(root)))