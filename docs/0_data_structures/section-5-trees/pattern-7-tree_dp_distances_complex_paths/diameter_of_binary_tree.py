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
    def diameter_of_binary_tree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(node):
            nonlocal max_diameter

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            max_diameter = max(max_diameter, left + right)

            return 1 + max(left, right)
        
        dfs(root)
        return max_diameter

root = [1,2,3,4,5]
print(Solution().diameterOfBinaryTree(build_tree(root)))