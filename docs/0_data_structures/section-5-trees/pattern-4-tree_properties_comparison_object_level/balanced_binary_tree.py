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
    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            if left == -1: return -1
            
            right = dfs(node.right)
            if right == -1: return -1
            
            if abs(left - right) > 1:
                return -1
            
            return 1 + max(left, right)
            
        return dfs(root) != -1

root = [3,9,20,None,None,15,7]
print(Solution().isBalanced(build_tree(root)))