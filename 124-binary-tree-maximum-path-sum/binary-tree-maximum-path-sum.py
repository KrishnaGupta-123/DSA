# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        maxpath = root.val
        def helper(node):
            nonlocal maxpath
            if not node:
                return 0
            left_path = helper(node.left)
            right_path = helper(node.right)
            left_max = max(left_path,0)
            right_max = max(right_path,0)
            maxpath = max(maxpath,node.val + left_max + right_max)
            return node.val + max(left_max,right_max)
        helper(root)
        return maxpath