# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 20 + 1, 2
# 21, +2 , 3
# 22, 4 ,5
# [1, 2, 3, 4, 5]

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""

        result = []
        bfs = deque([root])

        while bfs:
            node = bfs.popleft()
            if node:
                result.append(str(node.val))
                bfs.append(node.left)
                bfs.append(node.right)
            else:
                result.append("#")
        finalString = ",".join(result)
        print("finalString",finalString)
        return finalString

    def deserialize(self, data2):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data2 == "":
            return None

        nodes = data2.split(",")
        
        i = 1

        root = TreeNode(int(nodes[0]))

        bfs = deque([root])

        while bfs:
            # print("root",root)
            node = bfs.popleft()
            node.left = None
            node.right = None
            # print("i left ", i)
            # print("nodes [i]", nodes[i])
        
            if i<len(nodes) and nodes[i] != "#":
                node.left = TreeNode(int(nodes[i]))
                bfs.append(node.left)
            i = i + 1
            # print("i right ", i)
            # print("nodes [i]", nodes[i])
            if i<len(nodes) and  nodes[i] != "#":
                node.right = TreeNode(int(nodes[i]))
                bfs.append(node.right)
            i = i + 1

        return root
                

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))