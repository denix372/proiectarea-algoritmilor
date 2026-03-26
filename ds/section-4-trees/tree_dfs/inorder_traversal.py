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

    child_index = 1
    for i in range(len(arr)):
        if nodes[i] is not None:
            if child_index < len(arr):
                nodes[i].left = nodes[child_index]
            child_index += 1

            if child_index < len(arr):
                nodes[i].right = nodes[child_index]
            child_index += 1

    return nodes[0]

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def solve(node):
            if not node:
                return
    
            solve(node.left)
            res.append(node.val)
            solve(node.right)
        
        solve(root)
        return res

root = [1,None,2,3]


print(Solution().inorderTraversal(build_tree(root)))