# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return []
        curr = head
        prev = None
        i = 0 
        while curr:
            i += 1
            curr = curr.next
        
        curr = head
        while curr:
            if i == n:
                if not prev:
                    curr = curr.next
                    return curr
            
                prev.next = curr.next

            i -= 1
            prev = curr
            curr = curr.next
        
        return head
