class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child:TreeNode):
        self.children.append(child)
        child.parent = self

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    def print_tree(self):
        level = self.get_level()
        spaces = "  " * level
        prefix = spaces + '|__' + self.data
        print(prefix)
        if self.children:
            for child in self.children:
                child.print_tree()
    def print_trees(self,node2):
        levelt1 = self.get_level()
        # levelt2 = node2.get_level()
        spaces = "  " * levelt1
        prefix = spaces + '|__' + self.data + "  " + f"({node2.data})" 
        print(prefix)
        if self.children :
            for child1 , child2 in zip(self.children,node2.children):
                child1.print_trees(child2)

        

def create_Tree(root,child1 , child2,child11 ,child12,child21,child22,child111,child112):

    root = TreeNode(root)

    chinmay = TreeNode(child1)
    Gels = TreeNode(child2)
    root.add_child(chinmay)
    root.add_child(Gels)

    vishwa = TreeNode(child11)
    aamir = TreeNode(child12)
    chinmay.add_child(vishwa)
    chinmay.add_child(aamir)

    dhaval = TreeNode(child111)
    abhijit = TreeNode(child112)

    vishwa.add_child(dhaval)
    vishwa.add_child(abhijit)
    peter = TreeNode(child21)
    waqas = TreeNode(child22)
    Gels.add_child(peter)
    Gels.add_child(waqas)
    return root
    

if __name__ == '__main__':
    root1 = create_Tree('Nilpul','Chinmay','Gels','Vishwa','Aamir','Peter','Waqas','Dhaval','Abhijit')
    root2 = create_Tree('CEO','CTO','HR HEAD','INFRASTRUCTURE HEAD','APPLICATION HEAD','RECRUITMENT MANAGER','POLICY MANAGER','CLOUD MANAGER','APP MANAGER')
    root1.print_tree()
    print("\n\n")
    root2.print_tree()
    print("\n\n")
    root1.print_trees(root2)


    
    
    
    