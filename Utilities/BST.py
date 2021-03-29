from collections import deque

class BST:
    class Node:
        # Initializing Binary tree node with data, left and right child
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self, value_list = []):
        self.root = None
        self.node_count = 0
        for data in value_list:
            self.insert(data)

    # Insertion in BST
    def insert(self, data):
        # If data already present
        if self.contains(data):
            return False
        self.root = self._insert_r(data, self.root)
        self.node_count += 1
        return True

    # Recursive function to insert in BST
    # Protected method
    def _insert_r(self, data, node):
        # Base case: found leaf node
        if node is None:
            return self.Node(data)
        if data < node.data:
            node.left = self._insert_r(data, node.left)
        else:
            node.right = self._insert_r(data, node.right)
        return node
        
    # Deletion in BST
    def remove(self, data):
        # if data is present
        if self.contains(data):
            self._remove_r(data, self.root)
            self.node_count -= 1
            return True
        return False

    # Recursive function to insert in BST
    def _remove_r(self, data, node):
        if node is None:    return None

        # Dig into(traverse) the tree to find the node we are looking for:
        if data < node.data:
            node.left = self._remove_r(data, node.left)
        elif data > node.data:
            node.right = self._remove_r(data, node.right)
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
                node.left = self._remove_r(new_node.data, node.left)
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
    # Used stack to append and pop data instead of recursive call - https://www.youtube.com/watch?v=nzmtCFNae9k
    def inorder_iterative(self):
        print_stack = list()
        node = self.root

        # do-while loop for print_stack != None
        while True:
            if node == None:
                # if stack and node is null, end the loop
                if len(print_stack) == 0: break

                node = print_stack.pop()
                print(node.data, end=' ')
                node = node.right
            else:
                print_stack.append(node)
                node = node.left
        print()

    # Printing the tree in lever order traversal
    # This is done using Breadth first search using a queue
    def level_order(self):
        print_queue = deque([self.root])

        while len(print_queue) > 0:
            parent = print_queue.popleft()
            print(parent.data, end=" ")
            if parent.left:
                print_queue.append(parent.left)
            if parent.right:
                print_queue.append(parent.right)
        print()

if __name__ == "__main__":
    # Testing BST
    #                   10
    #           7                 16
    #       3         9        14
    #   1     5     8       12    15
    #          6              13
    a = BST([10,7,3,1,5,6,9,8,16,14,12,13,15])
    a.level_order()
