from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        print("[]")
        return

    res = []
    q = deque([root])

    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)

    while res and res[-1] is None:
        res.pop()

    print(res)

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def convert(left, right):            
            if left > right:
                return

            mid = (left + right) // 2

            node = TreeNode(nums[mid])

            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)

            return node
        
        return convert(0, len(nums) - 1)

nums = [-10,-3,0,5,9]
print_tree(Solution().sortedArrayToBST(nums))