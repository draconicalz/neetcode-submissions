"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        oldToCopy = {}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next =  oldToCopy[cur.next] if oldToCopy.get(cur.next) else None
            copy.random = oldToCopy[cur.random] if oldToCopy.get(cur.random) else None
            cur = cur.next

        
        return oldToCopy[head]