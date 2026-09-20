# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        pt1 = list1
        pt2 = list2
        head = None
        current = head
        while pt1 and pt2:
            if pt1.val <= pt2.val:
                if not current:
                    current = pt1
                    head = current
                else:
                    current.next = pt1
                    current = current.next
                pt1 = pt1.next
            else:
                if not current:
                    current = pt2
                    head = current
                else:
                    current.next = pt2
                    current = current.next
                pt2 = pt2.next

        while not pt1 and pt2:
            if not current:
                    current = pt2
                    head = current
            else:
                current.next = pt2
                current = current.next
            pt2=pt2.next
        while not pt2 and pt1:
            if not current:
                    current = pt1
                    head = current
            else:
                current.next = pt1
                current = current.next
            pt1 = pt1.next

        return head