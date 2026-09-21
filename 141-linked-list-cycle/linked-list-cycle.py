# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current_next_set = set()
        current = head
        if not head :
            return False
        current = head
        while current.next:
            if current.next in current_next_set:
                return True
            current_next_set.add(current.next)
            current = current.next
        return False
