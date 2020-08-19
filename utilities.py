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
        