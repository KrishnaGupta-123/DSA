# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findGN(self,root: TreeNode,maxVal : int):
            if not root:
                return 0
            elif root.val < maxVal:
                return self.findGN(root.left,maxVal) + self.findGN(root.right,maxVal)
            else:
                return 1 + self.findGN(root.left,root.val) + self.findGN(root.right,root.val)

    def goodNodes(self, root: TreeNode) -> int:
        return self.findGN(root,root.val)