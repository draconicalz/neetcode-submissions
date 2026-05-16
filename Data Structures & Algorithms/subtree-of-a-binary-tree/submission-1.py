# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root, subRoot):
            if not root and not subRoot:
                return True
            elif root and subRoot and root.val == subRoot.val:
                return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)
            else:
                return False
        
        def dfs(root, subRoot):
            if root and subRoot and root.val == subRoot.val:
                if (isSameTree(root, subRoot)):
                    return True
                else:
                    return dfs(root.left, subRoot) or dfs(root.right, subRoot)
            elif not root:
                return False
            else:
                return dfs(root.left, subRoot) or dfs(root.right, subRoot)

        return dfs(root, subRoot)