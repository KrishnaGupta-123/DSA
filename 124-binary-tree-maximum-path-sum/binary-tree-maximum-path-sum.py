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
            left_path = node.val + helper(node.left)
            right_path = node.val + helper(node.right)
            total_path = left_path + right_path - node.val
            curr_max_path = max(left_path,right_path,total_path,node.val)
            maxpath = max(maxpath,curr_max_path)
            return max(left_path,right_path,node.val)
        helper(root)
        return maxpath