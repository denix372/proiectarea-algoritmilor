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

def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)

class Solution:
    def lowest_common_ancestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

root = build_tree([6,2,8,0,4,7,9,None,None,3,5])
p = find_node(root, 2)
q = find_node(root, 8)
print(Solution().lowestCommonAncestor(root, p, q).val)
