from typing import Optional

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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def solve(node):
            nonlocal max_sum
            if not node:
                return 0

            left = max(solve(node.left), 0)
            right = max(solve(node.right), 0)

            path = left + node.val + right

            max_sum = max(max_sum, path)

            return node.val + max(left, right)
            
        solve(root)
        return max_sum

root = [1,2,3]
print(Solution().maxPathSum(build_tree(root)))