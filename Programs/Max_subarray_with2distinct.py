'''
Given an array of integers what is the length of the longest subArray containing no more than two 
distinct values such that the distinct values differ by no more than 1
For Example:
arr = [0, 1, 2, 1, 2, 3] -> length = 4; [1,2,1,2]
arr = [1, 2, 3, 4, 5] -> length = 2; [1,2]
arr = [1, 1, 1, 3, 3, 2, 2] -> length = 4; [3,3,2,2]

arr = [1, 1, 2, 2, 1, 2, 3, 3, 2, 2, 3, 3] -> length = 7; [2, 3, 3, 2, 2, 3, 3]
'''

# def get_max_len(arr):
#     # code here
#     # dict containing the last occurance of that element
#     elem = {arr[0]:0}
#     max_len = 0
#     first = 0
#     for i in range(1,arr):
#         if arr[i] in elem:
#             # Storing the latest occurence
#             elem[arr[i]] = i
#         else:
#             for ele in elem:
#                 if abs(arr[i] - ele)==1:
#                     if len(elem) == 1:
#                         max_len = max(max_len, i+1)
#                         elem[arr[i]] = i
#                     elif len(elem) == 2:
#                         max_len = max(max_len, i-first)
#                         # Deleted the previous element and arr[i] is added to elem
#                         elem = {ele:elem[ele], arr[i]:i}
#                     break
#                 else:
#                     if len(elem)==1:
#                         elem = {arr[i]:i}
#                     if len(elem) == 2:
     
    
# # Contains the value and its first and last occurence in the list
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.last = None
#         self.next = None

# class Queue:
#     def __init__(self):
#         self.head = None
    
#     def insert(self, val):
#         if self.head == None:
#             self.head = Node(val, first)
#         else:
#             new_node = Node(val, first)
#             self.head.next = new_node
    

arr = list(map(int, input().strip().split()))
print(get_max_len(arr))