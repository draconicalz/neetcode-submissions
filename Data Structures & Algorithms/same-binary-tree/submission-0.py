# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []
        def dfs(root, tree):
            if not root:
                tree.append(None)
                return
            tree.append(root.val)

            dfs(root.left, tree)
            dfs(root.right, tree)

        dfs(p, tree1)
        dfs(q, tree2)

        return tree1 == tree2 


            