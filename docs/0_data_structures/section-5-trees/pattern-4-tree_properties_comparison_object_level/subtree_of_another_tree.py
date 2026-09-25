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
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        return (p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right))
    
    def is_subtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        
        return (self.isSameTree(root, subRoot) or
                self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

root = [3,4,5,1,2]
subRoot = [4,1,2]
print(Solution().isSubtree(build_tree(root), build_tree(subRoot)))