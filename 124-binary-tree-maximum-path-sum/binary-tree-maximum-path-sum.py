# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=-math.inf

        def search(node):
            nonlocal ans
            if node is None:
                return 0
            let=search(node.left)
            rit=search(node.right)
            mid=node.val+let+rit
            ans=max(mid,ans)
            return max(node.val+max(let,rit),0)
        search(root)
        return ans

            

        