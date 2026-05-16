# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        fast = head
        slow = head

        fast = head.next 
        if fast:
            fast = fast.next
            if not fast:
                return False
        else:
            return False
        slow = head.next

        while fast != slow:
            fast = fast.next
            if fast:
                fast = fast.next
                if not fast:
                    return False
            else:
                return False
            slow = slow.next
        
        return True
