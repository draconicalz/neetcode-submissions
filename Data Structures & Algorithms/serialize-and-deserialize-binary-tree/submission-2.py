# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res = ""
        q = deque()
        q.append(root)

        while q:
            cur = q.popleft()

            if not cur:
                res += "N"
                continue

            res += str(cur.val) + "."
            q.append(cur.left)
            q.append(cur.right)

        return res



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        root = None
        cur = ""
        qToChild = deque()
        for c in data:
            if c not in [".", "N"]: cur += c
            elif c == ".":
                # create node
                value = int(cur)
                cur = ""
                node = TreeNode()
                node.val = value
                if not root: root = node

                # add children
                if qToChild:
                    if qToChild[0][1] == 1: 
                        qToChild[0][0].left = node
                        qToChild[0][1] -= 1
                    elif qToChild [0][1] == 0:
                        qToChild[0][0].right = node
                        qToChild.popleft()

                # assign to get children
                qToChild.append([node, 1])
            elif c == "N":
                # add null
                if qToChild:
                    if qToChild[0][1] == 1: 
                        qToChild[0][0].left = None
                        qToChild[0][1] -= 1
                    elif qToChild [0][1] == 0:
                        qToChild[0][0].right = None
                        qToChild.popleft()
        return root


