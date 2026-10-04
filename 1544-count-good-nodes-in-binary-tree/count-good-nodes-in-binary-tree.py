# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findGN(self,root: TreeNode,maxVal : int):
            count = 0
            if not root:
                return 0
            if root.val >= maxVal:
                maxVal = root.val
                count += 1
            count = count + self.findGN(root.left,maxVal)
            count = count + self.findGN(root.right,maxVal)
            return count
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        maxVal = root.val
        return self.findGN(root,maxVal)