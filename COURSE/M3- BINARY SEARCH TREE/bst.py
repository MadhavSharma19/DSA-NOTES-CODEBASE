# Topic: Inorder Traversal in Binary Search Tree (BST)

# Creating node class
class BSTNode:

    # Constructor
    def __init__(self, data):

        # Storing data
        self.data = data

        # Left child
        self.left = None

        # Right child
        self.right = None


# Function for inorder traversal
def inorder(root):

    # Base condition
    # Stop if node becomes None
    if root == None:
        return

    # Visit left subtree first
    inorder(root.left)

    # Print root node
    print(root.data, end=" ")

    # Visit right subtree
    inorder(root.right)


# Creating nodes manually
root = BSTNode(10)

root.left = BSTNode(20)
root.right = BSTNode(30)

root.left.left = BSTNode(40)
root.left.right = BSTNode(50)

# Calling inorder traversal
inorder(root)