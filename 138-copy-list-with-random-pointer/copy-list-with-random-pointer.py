"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        ncurr = Dummy = Node(0)
        nodelist = []
        Nnodelist = []
        while curr:
            nodelist.append(curr)
            Nnew = Node(curr.val)
            ncurr.next = Nnew
            ncurr = ncurr.next
            Nnodelist.append(ncurr)
            curr = curr.next
        t = 0
        n = len(nodelist)
        while t != n:
            targetnode = nodelist[t].random
            if targetnode is not None:
                idx = [i for i,node in enumerate(nodelist) if node is targetnode]
                Nnodelist[t].random = Nnodelist[idx[0]]
            t += 1
        return Dummy.next



