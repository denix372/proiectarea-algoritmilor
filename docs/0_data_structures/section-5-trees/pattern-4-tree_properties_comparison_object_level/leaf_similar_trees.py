from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
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
    def leaf_similar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def childs(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            return childs(root.left) + childs(root.right)
        
        ch1 = childs(root1)
        ch2 = childs(root2)

        if len(ch1) != len(ch2):
            return False
    
        return all( c1 == c2 for c1, c2 in zip(ch1, ch2))

root1 = [3,5,1,6,2,9,8,None,None,7,4]
root2 = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
print(Solution().leafSimilar(build_tree(root1), build_tree(root2)))