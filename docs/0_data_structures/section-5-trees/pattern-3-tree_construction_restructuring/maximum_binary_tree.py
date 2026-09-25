from typing import List, Optional
from collections import deque

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
    def construct_maximum_binary_tree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mx = max(nums)
        i = nums.index(mx)
        node = TreeNode(mx)
        node.left = self.constructMaximumBinaryTree(nums[:i])
        node.right = self.constructMaximumBinaryTree(nums[i + 1:])
        return node
nums = [3,2,1,6,0,5]
print_tree(Solution().constructMaximumBinaryTree(nums))