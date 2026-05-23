# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []
        res = None
        def dfs(node):
            nonlocal res
            if node.left:
                dfs(node.left)
            
            if res != None: return res
            nums.append(node.val)
            if len(nums) == k:
                res = nums[-1]
                return res
            if node.right:
                dfs(node.right)
            if res != None: return res

        return dfs(root)