# Topic: Postorder Traversal in Binary Search Tree (BST)

# Creating node class
class BSTNode:

    # Constructor
    def __init__(self, data):

        # Storing data inside node
        self.data = data

        # Left child node
        self.left = None

        # Right child node
        self.right = None


# Function for postorder traversal
def postorder(root):

    # Base condition
    # Stop recursion if node becomes None
    if root == None:
        return

    # Visit left subtree first
    postorder(root.left)

    # Visit right subtree
    postorder(root.right)

    # Print root node at last
    print(root.data, end=" ")


# Creating nodes manually
root = BSTNode(10)

root.left = BSTNode(20)
root.right = BSTNode(30)

root.left.left = BSTNode(40)
root.left.right = BSTNode(50)

# Calling postorder traversal
postorder(root)