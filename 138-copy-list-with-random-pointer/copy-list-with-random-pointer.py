"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldtocopy = defaultdict(lambda : Node(0))
        oldtocopy[None] = None
        curr = head
        while curr:
            oldtocopy[curr].val = curr.val
            oldtocopy[curr].next = oldtocopy[curr.next]
            oldtocopy[curr].random = oldtocopy[curr.random]
            curr = curr.next
        return oldtocopy[head]
