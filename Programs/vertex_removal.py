# You are given an  polygon where vertices are numbered from 1 to  in clockwise order, You are also given an integer . You create a vertex-explosion machine that explodes vertex in polygon thereby reducing the size of the polygon. You start with vertex 2.  At each step, one of the following operations on the polygon is performed:

# If , then there is no effect of the vertex-explosion machine. Now,  is reduced by 1 and you move to the next available vertex at distance 2 in the clockwise direction.
# The vertex is exploded thus reducing the number of sides in the polygon by 1 and you move to the next available vertex at distance 2 in the clockwise direction from the exploded vertex. 
# Note: Polygon with vertex 2 and 1 exists

def remove_vertex(N, K):
    if K > 0:
        return (remove_vertex(N, K-1) + 1)%N +1
    else:
        if N == 1:
            return 1
        else:
            return (remove_vertex(N-1, 0) + 1)%N +1

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N, K = map(int, input().rstrip().split())
        print(remove_vertex(N, K)+1)

# By Linked list 

# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def last_vertex(N, K):
#     # creating the list
#     head = node(1)
#     ptr = head
#     for i in range(2, N+1):
#         nnode = node(i)
#         ptr.next = nnode
#         ptr = ptr.next
#     ptr.next = head

#     ptr = head.next
#     while N>1:
#         if K >0:
#             prev = ptr.next
#             ptr = prev.next
#             K -= 1
#         else:
#             prev.next = ptr.next
#             prev = prev.next
#             ptr = prev.next
#             N-=1
#     return ptr.data
