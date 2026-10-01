# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        hb = True
        def heightcheck(root):
            nonlocal hb
            if not root:
                return 0
            left = heightcheck(root.left)
            right = heightcheck(root.right)
            if abs(right - left) > 1:
                hb = False
                return 0
            return max(left,right) + 1
        heightcheck(root)
        return hb