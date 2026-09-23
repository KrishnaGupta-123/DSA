# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        start_node = ListNode()
        prev = start_node
        
        carry = 0
        while l1 or l2:
            if not l1:
                l1_val = 0
                
            else:
                l1_val = l1.val
                l1 = l1.next
            if not l2:
                l2_val = 0
            else:
                l2_val = l2.val
                l2 = l2.next
                
                
            sum = l1_val + l2_val
            if carry:
                sum += 1
                carry = 0
                
            if sum >= 10:
                sum -= 10
                carry = 1

            
            new_node = ListNode(sum)
            prev.next = new_node
            prev = new_node
            
        if carry:
            prev.next = ListNode(1)
        
            
        return start_node.next