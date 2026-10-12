# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:




        def dfs(curr, low, high):


            if not curr:
                return True

            
            if low >= curr.val or high <= curr.val:
                return False
            


            if not dfs(curr.left, low, curr.val):
                return False
            
            if not dfs(curr.right, curr.val, high):
                return False

            return True
        

        return dfs(root, float("-inf"), float("inf"))
            
        