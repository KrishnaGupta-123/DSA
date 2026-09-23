# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        curr1 = l1
        str1 = ""
        while curr1:
            str1 += str(curr1.val)
            curr1 = curr1.next
        curr2 = l2
        str2 = ""
        while curr2:
            str2 += str(curr2.val)
            curr2 = curr2.next
        total = str(int(str1[::-1]) + int(str2[::-1]))
        n = len(total)
        i=-1
        newHead = None
        curr = None
        while i != -(n+1):
            newNode = ListNode(int(total[i]))
            if not newHead:
                newHead = newNode
                curr = newNode
            else:
                curr.next = newNode
                curr = curr.next
            i -= 1
        return newHead
