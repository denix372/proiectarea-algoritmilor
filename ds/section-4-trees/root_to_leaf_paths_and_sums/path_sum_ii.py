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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        res = []
        def dfs(node, s, sol):
            if not node:
                return

            if (node
                and not node.right
                and not node.left
                and node.val + s == targetSum):
                    sol = sol + [node.val]
                    res.append(sol.copy())
                    return
    
            dfs(node.left, s + node.val, sol + [node.val])
            dfs(node.right, s + node.val, sol + [node.val])

        dfs(root, 0, [])
        return res

root = [5,4,8,11,None,13,4,7,2,None,None,5,1]
targetSum = 22
print(Solution().pathSum(build_tree(root), targetSum))