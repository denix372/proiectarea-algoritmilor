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
    def is_mirror(self, left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val
                    and self.isMirror(left.left, right.right)
                    and self.isMirror(left.right, right.left))

    def is_symmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

root = [1,2,2,3,4,4,3]
print(Solution().isSymmetric(build_tree(root)))