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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 or l2 or carry != 0:
            if l1 is not None:
                digit1 = l1.val
            else:
                digit1 = 0
            
            if l2 is not None:
                digit2 = l2.val
            else:
                digit2 = 0
            
            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            tail.next = ListNode(digit)
            tail = tail.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        result = dummyHead.next
        dummyHead.next = None
        return result

l1 = [2,4,3]
l2 = [5,6,4]
print_list(Solution().addTwoNumbers(build_list(l1), build_list(l2)))