import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Reservoir Sampling
class Solution:

    def __init__(self, head: ListNode | None):
        self.head = head

    def getRandom(self) -> int:
        cnt = 0
        res = 0
        node = self.head

        while node:
            cnt += 1
            if random.randint(1, cnt) == 1:
                res = node.val
            node = node.next
        
        return res

def build_list(arr):
    dummy = ListNode()
    tail = dummy
    for x in arr:
        tail.next = ListNode(x)
        tail = tail.next
    return dummy.next

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

solution = Solution(build_list([1, 2, 3]))
print(solution.getRandom()) # return 1
print(solution.getRandom()) # return 3
print(solution.getRandom()) # return 2
print(solution.getRandom()) # return 2
print(solution.getRandom()) # return 3
# getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
 
'''
INTERVIEW FOLLOW-UP ANSWERS:

Q1: What if the linked list is extremely large and its length is unknown to you?
Q2: Could you solve this efficiently without using extra space?

Answer:
We use an algorithm called Reservoir Sampling. The goal of Reservoir Sampling is to 
choose k items (here k = 1) from a stream of items of unknown length with equal probability.

How it works:
1. When we see the 1st node, we pick it with probability 1/1 (100%).
2. When we see the 2nd node, we replace our choice with the 2nd node with probability 1/2.
3. When we see the i-th node, we replace our current choice with the i-th node with probability 1/i.

Mathematical Proof of Equal Probability:
What is the probability that the k-th node is the final chosen answer in a list of N nodes?
It requires two things to happen:
1. We pick the k-th node when we are at step k (Probability: 1/k).
2. We DO NOT replace it at step k+1, step k+2, ... up to step N.
   - Probability of NOT replacing at step k+1 is 1 - (1/(k+1)) = k / (k+1)
   - Probability of NOT replacing at step k+2 is 1 - (1/(k+2)) = (k+1) / (k+2)
   
Multiplying these independent probabilities:
P = (1 / k) * (k / (k+1)) * ((k+1) / (k+2)) * ... * ((N-1) / N)

The numerators and denominators cancel each other out sequentially (telescoping product), 
leaving exactly: P = 1 / N.
Thus, every node has the exact same uniform probability of 1/N of being selected, 
using exactly O(1) auxiliary space and O(N) time per getRandom() call.
'''