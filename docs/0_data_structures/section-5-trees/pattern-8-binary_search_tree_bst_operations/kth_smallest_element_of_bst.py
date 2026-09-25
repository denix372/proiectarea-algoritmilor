from typing import List, Optional
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

class Solution:
    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        
        def inorder(node):
            nonlocal k, res
            
            if not node or res is not None:
                return
            
            inorder(node.left)
            
            k -= 1
            if k == 0:
                res = node.val
                return

            inorder(node.right)
            
        inorder(root)
        return res

root = [3,1,4,None,2]
k = 1
print(Solution().kthSmallest(build_tree(root), k))