# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        while head:
            tempNext = head.next
            if last:
                head.next = last
            else:
                head.next = None
            last = head
            head = tempNext
        return last