# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        addr = []
        current = head
        while current.next:
            addr.append(current.next)
            current = current.next
        
        i ,j = 0 , len(addr) - 1
        curr = head
        curr.next = None
        chance_of_i = 0
        while i<=j:
            if chance_of_i:
                curr.next = addr[i]
                curr = curr.next
                i += 1
                chance_of_i = 0
            else: 
                curr.next = addr[j]
                curr = curr.next
                j -= 1
                chance_of_i = 1
        curr.next = None
        