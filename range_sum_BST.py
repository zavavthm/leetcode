from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def sumBST(root):
            if root is None:
                return 0
            sum = 0
            if root.val < low:
                return sumBST(root.right)
            elif root.val > high:
                return sumBST(root.left)
            sum += root.val
            sum += sumBST(root.left)
            sum += sumBST(root.right)
            return sum
        return sumBST(root)

obj = Solution()
low = 5
high = 15
root = TreeNode(10)

print(obj.rangeSumBST(root, low, high))