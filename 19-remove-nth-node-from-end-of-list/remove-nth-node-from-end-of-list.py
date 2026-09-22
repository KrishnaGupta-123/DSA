# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        current = head
        addr = []
        while current:
            addr.append(current)
            current = current.next
        if n == 1 and len(addr) == 1:
            head = None
        elif n==1:
            addr[-(n+1)].next = None
        elif n == len(addr):
            temp = head
            head = head.next
            temp.next = None
        else:
            addr[-(n+1)].next = addr[-(n-1)]
            addr[-n].next = None
        return head
