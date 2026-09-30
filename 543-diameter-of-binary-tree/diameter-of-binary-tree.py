# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def mxd(root):
            nonlocal res

            if not root:
                return 0
            left = mxd(root.left)
            right = mxd(root.right)
            res = max(res,left + right)

            return max(left,right) + 1
        mxd(root)
        return res