from typing import List, Optional
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def build_tree(arr):
    if not arr:
        return None

    root = Node(arr[0])
    q = deque([root])
    i = 2 

    while q and i < len(arr):
        parent = q.popleft()
        children = []

        while i < len(arr) and arr[i] is not None:
            child = Node(arr[i])
            children.append(child)
            q.append(child)
            i += 1

        parent.children = children
        i += 1

    return root

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        mx = 0
        for ch in root.children:
            mx = max(mx,self.maxDepth(ch))
        return 1 + mx

root = [1,None,3,2,4,None,5,6]
print(Solution().maxDepth(build_tree(root)))