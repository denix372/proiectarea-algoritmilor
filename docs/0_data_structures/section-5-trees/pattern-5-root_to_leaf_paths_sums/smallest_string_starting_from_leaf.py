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
    def smallest_from_leaf(self, root: Optional[TreeNode]) -> str:
        res = None
        def dfs(node, path):
            nonlocal res
            if not node:
                return
            
            if not node.left and not node.right:
                path = path + chr(97 + node.val)
                if res:
                    res = min(res, path[::-1])
                else:
                    res = path[::-1]
                return

            dfs(node.left, path + chr(97 + node.val) )
            dfs(node.right, path + chr(97 + node.val) )
        
        dfs(root, "")
        return res

root = [0,1,2,3,4,3,4]
print(Solution().smallestFromLeaf(build_tree(root)))