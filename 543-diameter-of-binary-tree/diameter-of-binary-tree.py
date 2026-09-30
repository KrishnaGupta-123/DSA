# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
max_d = 0
class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.max_depth(root.left),self.max_depth(root.right)) + 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depthL = self.max_depth(root.left)
        depthR = self.max_depth(root.right)
        max_d = depthL + depthR
        sub = max(self.diameterOfBinaryTree(root.left),
                  self.diameterOfBinaryTree(root.right))
        return max(max_d, sub)



        