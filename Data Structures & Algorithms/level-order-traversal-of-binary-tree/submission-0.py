# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            curQueue = deque()
            level = []
            while queue:
                node = queue.popleft()
                level.append(node.val)
                if node.left: curQueue.append(node.left)
                if node.right: curQueue.append(node.right)

            res.append(level)
            queue = curQueue

        return res