''' Contains the utility functions useful for CP '''

import math

# Check if prime or not
def isprime(n):
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n))+2):
        if n%i == 0:
            return False
    return True

# Binary search
def binary_search(arr, target):
    left = 0
    right = len(arr)
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid +1
        else:
            right = mid -1
    return -1

# Returns factorial
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

# Return gcd of 2 nums
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

# Using seive of erasthanos to get all prime numbers till n
def get_primes(n):
    primes = [True for i in range(n)]
    for i in range(2, int(math.sqrt(n))+2):
        if primes[i-1]:
            j = i**2
            while j <= n:
                primes[j-1] = False
                j += i
    result = []
    for i in range(1, len(primes)):
        if primes[i]:
            result.append(i+1)
    return result

# Linked list implementation 
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
        # self.tail = None  # uncomment for queue
    
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
    
    def push(self, new_node:Node):
        if self.head:
            new_node.next = self.head
        self.head = new_node
        return self.head
    
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
    
    def push(self, new_node:Node):
        if self.head == None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return self.tail
    
    def pop(self):
        if self.head:
            popped = self.head
            self.head = self.head.next
            popped.next = None
            return popped.data
        else:
            print("Stack Underflow")
            return None
