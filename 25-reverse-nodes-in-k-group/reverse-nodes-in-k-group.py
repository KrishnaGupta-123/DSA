# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_kth_node(self, curr: ListNode | None, k: int) -> ListNode | None:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if k==1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        while True:
            end = self.get_kth_node(start, k)
            if not end:
                break
            
            group_next = end.next
            prev = end.next
            curr = start.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = start.next
            start.next = end
            start = temp
        return dummy.next