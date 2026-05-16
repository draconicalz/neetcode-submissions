# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        rightDepth = 0
        leftDepth = 0

        if root.left:
            leftDepth = self.maxDepth(root.left) + 1
        if root.right:
            rightDepth = self.maxDepth(root.right) + 1
        
        if not root.left and not root.right:
            return 1
        
        return max(leftDepth, rightDepth)