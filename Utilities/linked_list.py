# Node structure for linked list
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked list implementation 
class Linked_list:
    def __init__(self):
        self.head = None
    
    # Insert at end
    def insert(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = Node(val)
        
class Stack:
    def __init__(self):
        self.head = None
    
    # Insert at beginning
    def push(self, new_node:Node):
        if self.head:
            new_node.next = self.head
        self.head = new_node
        return self.head
    
    # Delete at beginning
    def pop(self):
        if self.head:
            popped = self.head
            self.head = self.head.next
            popped.next = None
            return popped.data
        else:
            print("Stack Underflow")
            return None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Insert at end(tail)
    def push(self, new_node:Node):
        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return self.tail
    
    # Delete at beginning
    def pop(self):
        if self.head:
            popped = self.head
            self.head = self.head.next
            popped.next = None
            return popped.data
        else:
            print("Queue Underflow")
            return None
