from typing import List, Optional

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
    def lca_deepest_leaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        max_len = 0

        def solve(node):
            if not node:
                return (0, None)

            lh, lp = solve(node.left)
            rh, rp = solve(node.right)
            
            if lh == rh:
                return lh + 1, node
            elif lh > rh:
                return lh + 1, lp
            else:
                return rh + 1, rp

        return solve(root)[1]