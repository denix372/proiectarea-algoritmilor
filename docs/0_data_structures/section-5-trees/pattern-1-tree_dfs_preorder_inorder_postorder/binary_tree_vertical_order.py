from typing import List, Optional
from collections import deque, defaultdict

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

def solve(root):
    q = deque([(root, 0)])
    d = defaultdict(list)

    while q:
        for _ in range(len(q)):
            node, i = q.popleft()
            if not node:
                continue
            
            d[i].append(node.val)
            q.append((node.left, i - 1))
            q.append((node.right, i + 1))

    return [v for _, v in sorted(d.items())]

root = [3,9,8,4,0,1,7,None,None,None,2,5]

print(solve(build_tree(root)))