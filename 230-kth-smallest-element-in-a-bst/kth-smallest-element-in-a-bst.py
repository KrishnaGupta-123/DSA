# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root: TreeNode | None):
        elements = []
        if root.left:
            elements += self.inorder(root.left)
        elements.append(root.val)
        if root.right:
            elements += self.inorder(root.right)
        return elements
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        res = self.inorder(root)
        return res[k-1]