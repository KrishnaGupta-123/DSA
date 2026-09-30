# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        depthL,depthR = 1,1
        depthL += self.maxDepth(root.left)
        depthR += self.maxDepth(root.right)
        return max(depthL,depthR)