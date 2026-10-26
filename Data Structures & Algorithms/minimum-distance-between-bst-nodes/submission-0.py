# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            arr.append(node.val)
            if node.right:
                dfs(node.right)
          
        dfs(root)
        minDiff = float("Inf")
        for i in range(len(arr)-1):
            minDiff = min(minDiff, abs(arr[i] - arr[i + 1]))
              
        return minDiff