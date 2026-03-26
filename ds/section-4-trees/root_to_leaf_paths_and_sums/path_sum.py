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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
    
        def dfs(node, s):
            if not node:
                return False
            if node and not node.right and not node.left:
                return node.val + s == targetSum
    
            return dfs(node.left, s + node.val) or dfs(node.right, s + node.val)
        
        return dfs(root, 0)

root = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 22
print(Solution().hasPathSum(build_tree(root), targetSum))