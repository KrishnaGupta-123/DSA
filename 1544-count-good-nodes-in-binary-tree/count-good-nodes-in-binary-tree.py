# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findGN(self,root: TreeNode,maxVal : int):
            res = []
            if not root:
                return res
            if root.val >= maxVal:
                maxVal = root.val
                res.append(maxVal)
            res = res + self.findGN(root.left,maxVal)
            res = res + self.findGN(root.right,maxVal)
            return res
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        maxVal = root.val
        return len(self.findGN(root,maxVal))