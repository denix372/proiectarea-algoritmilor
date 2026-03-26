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
    def merge(self, list1, list2):
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

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right = slow.next
        slow.next = None
        s = self.sortList(head)
        r = self.sortList(right)
        return self.merge(s, r)

head = [4,2,1,3]
print_list(Solution().sortList(build_list(head)))