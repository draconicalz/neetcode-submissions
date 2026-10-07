# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1: return root2
        if not root2: return root1
        # traverse tree 2 and attempts to follow the same path in 1
        def traverse(node1, node2):
            node1.val += node2.val
            
            if node2.right:
                if not node1.right:
                    node1.right = node2.right
                else:
                    traverse(node1.right, node2.right)
            if node2.left:
                if not node1.left:
                    node1.left = node2.left
                else:
                    traverse(node1.left, node2.left)
            
        traverse(root1, root2)
        return root1