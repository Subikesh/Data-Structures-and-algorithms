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
    def insert(self, strr, num_insertions = 1):
        if strr is None:
            raise ValueError("strr cannot be NULL")
        if num_insertions <= 0:
            raise ValueError("num_insertions cannot be 0 or less than 0")
        
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

            # Increase the count of word occurence in the prefix-node
            node.count += num_insertions

        # Root cannot be word ending... It is just placeholder
        if node != self.root: node.ending = True
        
        # Return true if word already present and new is not created
        return is_prefix or not created_new_node

    # This deletes keys from the trie (even those which are not yet inserted)
    # This means that it may be the case that you delete a prefix which
    # cuts off the access to numerous other strings starting with that prefix.
    def delete(self, strr, num_deletions = 1):

        if not self.contains(strr):
            return False
        if num_deletions <= 0:
            raise ValueError("num_deletions cannot be 0 or less than 0")
        
        node = self.root
        for ch in strr:
            curr_node = node.children[ch]
            curr_node.count -= num_deletions

            # if all the prefixes below this are to be deleted
            # Cut the children off
            if curr_node.count <= 0:
                del node.children[ch]
                curr_node.children = None
                curr_node = None
                return True

            node = curr_node

        return True

    # Returns if strr is in the trie
    def contains(self, strr):
        return self.count(strr) > 0
    
    # Returns the number of times strr occurs in trie
    def count(self, strr):
        node = self.root

        # Dig down trie to find the full string or reach leaf node
        for ch in strr:
            node = node.children.get(ch, -1)
            # If node not present
            if node == -1:
                return 0
        else:
            return node.count
