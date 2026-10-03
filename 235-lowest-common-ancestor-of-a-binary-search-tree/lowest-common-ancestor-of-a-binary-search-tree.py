# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        AOP = set()
        temp = root
        while True:
            if temp.val > p.val:
                AOP.add(temp)
                temp = temp.left
            elif temp.val < p.val:
                AOP.add(temp)
                temp  = temp.right
            else:
                #temp.val == p.val
                AOP.add(temp)
                break
            
        temp = root
        LCA = root
        while True:
            if temp.val > q.val:
                if temp in AOP:
                    LCA = temp
                temp = temp.left
            elif temp.val < q.val:
                if temp in AOP:
                    LCA = temp
                temp = temp.right
            else:
                #temp.val == q.val
                if temp in AOP:
                    LCA = temp
                break
        return LCA