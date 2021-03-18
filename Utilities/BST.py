class Node:
    # Initializing Binary tree with data, left and right child
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:

    def __init__(self):
        self.root = None
        self.node_count = 0

    # Insertion in BST
    def insert(self, data):
        # If data already present
        if self.contains(data):
            return False
        self.root.insert_r(data, self.root)
        self.node_count += 1
        return True

    # Recursive function to insert in BST
    def insert_r(self, data, node):
        # Base case: found leaf node
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self.insert_r(data, node.left)
        else:
            node.right = self.insert_r(data, node.right)
        return node
        
    # Deletion in BST
    def remove(self, data):
        # if data is present
        if self.contains(data):
            self.remove_r(data, self.root)
            self.node_count -= 1
            return True
        return False

    # Recursive function to insert in BST
    def remove_r(self, data, node):
        if node is None:    return None

        # Dig into(traverse) the tree to find the node we are looking for:
        if data < node.data:
            node.left = self.remove_r(data, node.left)
        elif data > node.data:
            node.right = self.remove_r(data, node.right)
        # if the node to be deleted is `node`
        else:

            # if left tree is null:
            if node.left is None:
                # Make current node as right tree                
                return node.left

            # If right tree is null
            elif node.right is None:
                # Make current node as left tree
                return node.right

            # If both sub-tree is present
            else:
                # Take the rightmost element of left sub-tree and replace it with current_node
                new_node = self.find_max(node.left)
                node.data = new_node.data
                # Remove the replaced node to avoid repetition
                node.left = self.remove_r(new_node.data, node.left)
        return node

    # To check if data is present in tree
    def contains(self, data):
        return self.contains_r(data, self.root)
    
    # Recursive function to search a data in BST
    def contains_r(self, data, node):
        if node is None:
            return False
        if node.data == data:
            return True
        if node.data < data:
            return self.contains_r(data, node.right)
        if node.data > data:
            return self.contains_r(data, node.left)

    # Helper function to find the max node in the tree
    def find_max(self, node):
        while node.right != None:
            node = node.right
        return node

    # Returns the max height of the tree
    def get_height(self):
        return self.height(self.root)
    
    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1

    # Printing the tree in left-child, parent, right-child order
    # Can be modified to make preorder and postorder traversels
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data)
            self.inorder_traversal(node.right)

    # Printing the tree inorder iteratively
    def inorder_iterative(self, node):
        print_stack = list()
        while True:
            

