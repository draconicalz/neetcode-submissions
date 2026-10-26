# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]
        next = []
        odd = False
        while q:
            cur = q.pop()
            
            if cur.left:
                next.append(cur.left)
            if cur.right:
                next.append(cur.right)
            
            if len(q) == 0:
                odd = not odd
                q = next.copy()
                next = []
                if odd:
                    for i in range(len(q)//2):
                        temp = q[i].val
                        q[i].val = q[-(i+1)].val
                        q[-(i+1)].val = temp
                
        return root