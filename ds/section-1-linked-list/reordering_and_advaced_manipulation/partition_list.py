from typing import Optional

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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        slist, blist = ListNode(), ListNode()
        small, big = slist, blist

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next

            head = head.next
        
        small.next = blist.next
        big.next = None

        return slist.next

head = [1,4,3,2,5,2]
x = 3
print_list(Solution().partition(build_list(head), x))