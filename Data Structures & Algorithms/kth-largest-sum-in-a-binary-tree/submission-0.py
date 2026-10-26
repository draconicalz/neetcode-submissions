# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        q = [root]
        next = []
        curSum = 0
        while q:
            node = q.pop()
            curSum += node.val
            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)
            
            if not q:
                q = next.copy()
                sums.append(curSum)
                curSum = 0
                next = []
        sums.sort()
        return sums[-k] if k <= len(sums) else -1