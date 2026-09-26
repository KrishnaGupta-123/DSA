class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if self.data == data:
            
            return

        if self.data > data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTNode(data)

    def inorderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inorderTraversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorderTraversal()

        return elements
    
    def preorderTraversal(self):
        elements = []
        elements.append(self.data)

        if self.left:
            elements += self.left.preorderTraversal()
        if self.right:
            elements += self.right.preorderTraversal()

        return elements
    
    def postorderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.postorderTraversal()
        if self.right:
            elements += self.right.postorderTraversal()
        elements.append(self.data)

        return elements
    
    def search(self,data):
        if self.data == data:
            return True
        if self.data > data:
            return self.left.search(data) if self.left else False
        else:
            return self.right.search(data) if self.right else False
        
    def find_min(self):
        while self.left:
            self = self.left
        return self.data
    
    def find_max(self):
        while self.right:
            self = self.right
        return self.data


def Build_Tree(elements):
    if not elements:
        return None
    root = BSTNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

def insert(root):
    numbers = list(
        map(int, input("Enter numbers separated by space: ").split())
    )

    for number in numbers:
        root.add_child(number)

    print(f"{len(numbers)} element(s) inserted successfully.")
    return True

def search(root):
    data = int(input("Enter element to search: "))

    if root.search(data):
        print(f"{data} found in the BST.")
    else:
        print(f"{data} not found in the BST.")

    return True

def inorder(root):
    print("Inorder:", root.inorderTraversal())


def preorder(root):
    print("Preorder:", root.preorderTraversal())


def postorder(root):
    print("Postorder:", root.postorderTraversal())


def find_min(root):
    print("Minimum:", root.find_min())


def find_max(root):
    print("Maximum:", root.find_max())

def display_menu():
    print("\n========== BST MENU ==========")
    print("1. Insert element")
    print("2. Search element")
    print("3. Inorder traversal")
    print("4. Preorder traversal")
    print("5. Postorder traversal")
    print("6. Find minimum")
    print("7. Find maximum")
    print("8. Exit")
    print("==============================")


if __name__ == "__main__":

    elements = list(
        map(int, input("Enter elements separated by space: ").split())
    )

    root = Build_Tree(elements)

    operations = {
        1: insert,
        2: search,
        3: inorder,
        4: preorder,
        5: postorder,
        6: find_min,
        7: find_max
    }

    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 8:
            print("Exiting...")
            break

        operation = operations.get(choice)
        if operation:
            operation(root)
        else:
            print("Invalid choice. Please try again.")