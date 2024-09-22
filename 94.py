from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        def inorderBT(root):
            if root:
                inorderBT(root.left)
                ls.append(root.val)
                inorderBT(root.right)
        inorderBT(root)
        return ls

obj = Solution()
root = TreeNode(12)
print(obj.inorderTraversal(root))
