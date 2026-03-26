from heapq import heappush, heappop
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(arr):
    dummy = ListNode()
    tail = dummy
    for x in arr:
        tail.next = ListNode(x)
        tail = tail.next
    return dummy.next

def print_list(node):
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    print(vals)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        for i, node in enumerate(lists):
            if node:
                heappush(q, (node.val, i, node))
        
        dummy = ListNode()
        tail = dummy

        while q:
            val, i, node = heappop(q)
            tail.next = node
            tail = tail.next

            if node.next:
                heappush(q, (node.next.val, i, node.next))
        return dummy.next

lists = [build_list([1,4,5]),build_list([1,3,4]),build_list([2,6])]
print_list(Solution().mergeKLists(lists))