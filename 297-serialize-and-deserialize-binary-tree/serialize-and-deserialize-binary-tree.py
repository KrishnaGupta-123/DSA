# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "*#"
        q = deque()
        strs = ""
        q.append(root)
        while q:
            node = q.popleft()
            if node is not None:
                q.append(node.left)
                q.append(node.right)
            if node:
                strs += str(node.val) + "#"
            else:
                strs += "*" + "#"
        return strs
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        i,j = 0,0
        n = len(data)
        while data[j] != '#':
            j += 1
        if data[i:j] != '*':
            root = TreeNode(int(data[i:j]))
        else:
            return None
        q = deque()
        q.append(root)
        i = j = j+1
        while j != n:
            node = q.popleft()
            while data[j] != '#':
                j += 1
            if data[i:j] != '*':
                node.left = TreeNode(int(data[i:j]))
                q.append(node.left)
            i=j=j+1
            while data[j] != '#':
                j += 1
            if data[i:j] != '*':
                node.right = TreeNode(int(data[i:j]))
                q.append(node.right)
            i=j=j+1
        return root

            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))