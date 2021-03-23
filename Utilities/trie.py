'''
Trie(Prefix tree) -Used to make string operations easier. 
Stores prefix of strings and the children will be concat of the parent.
If node is final node.. traverse from root to leaf will be complete word
https://youtu.be/zIjfhVPRZCg
'''

class Trie:

    def __init__(self):
        self.root_char = '\0'
        self.root = self.Node(self.root_char)

    # Node structure for trie
    class Node:    
        def __init__(self, ch):
            # Charector of node
            self.ch = ch
            # Number of times this prefix has occured in array
            self.count = 0
            # bool if word ends or not
            self.ending = False
            # All children of the node
            self.children = {}

        def add_child(self, node, ch):
            self.children[ch] = node
    
    # Insert new string 
    def insert(self, strr):
        if strr is None:
            raise ValueError("strr cannot be NULL")
        
        node = self.root
        created_new_node = False    # Flag if new node created
        is_prefix = False           # Flag if strr prefix already present

        for ch in strr:
            next_node = node.children.get(ch, -1)

            # If next charector is not present in trie
            if next_node == -1:
                next_node = self.Node(ch)
                node.add_child(next_node, ch)
                created_new_node = True
            # Next charector exists in trie
            else:
                if next_node.ending: is_prefix = True

            node = next_node
            node.count += 1

        # Root cannot be word ending... It is just placeholder
        if node != self.root: node.ending = True
        
        # Return true if word already present and new is not created
        return is_prefix or not created_new_node

