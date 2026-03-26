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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        aux = dummy
        p = list1
        q = list2

        while p and q:
            if p.val < q.val:
                aux.next = p
                p = p.next
            else:
                aux.next = q
                q = q.next
            aux = aux.next

        aux.next = p if p else q
    
        return dummy.next

list1 = [1,2,4]
list2 = [1,3,4]
print_list(Solution().mergeTwoLists(build_list(list1), build_list(list2)))