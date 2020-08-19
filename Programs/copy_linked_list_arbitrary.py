#User function Template for python3

def copyList(head):
    '''
    param: head:  head of linkedList to copy
    return: the head of the copied linked list the #output will be 1 if successfully copied
    '''
    main_ptr = head
    copy = LinkedList()
    copy_ptr = copy.head
    # Copying the data and next pointer as in main LL
    while main_ptr.next != None:
        nnode = Node(main_ptr.data)
        if copy_ptr != None:
            copy_ptr.next = nnode
            copy_ptr = nnode
        else:
            copy.head = nnode
        main_ptr = main_ptr.next
    # Giving the link to and fro copy and main
    main_ptr = head
    copy_ptr = copy.head
    next_main = head
    while main_ptr != None:
        copy_ptr.arb = main_ptr
        next_main = main_ptr.next
        main_ptr.next = copy_ptr
        copy_ptr = copy_ptr.next
        main_ptr = next_main
    # Copying the arbitrary pointer of copy to appropriate values
    main_ptr = head
    copy_ptr = copy.head
    while copy_ptr != None:
        copy_ptr.arb = copy_ptr.arb.arb.next
        copy_ptr = copy_ptr.next
    return copy.head

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.arb=None
        
class LinkedList:
    def __init__(self):
        self.head = None

def insert(tail,data):
    tail.next=Node(data)
    return tail.next
    

def setarb(head,a,b):
    h=head
    i=1
    while i<a and h:
        h=h.next
        i+=1
    an=h
    
    h=head
    i=1
    while i<b and h:
        h=h.next
        i+=1
        
    if an:
        an.arb=h
        
def validation(head,res):
    
    while head and res:
        if id(head)==id(res):
            return
        
        #print(head.data,res.data,end=' ')
        if head.data != res.data:
            return
        
        if head.arb:
            if not res.arb:
                return
            
            #print(head.arb.data,res.arb.data)
            if head.arb.data != res.arb.data:
                return
            
        elif res.arb:
            return
        head=head.next
        res=res.next
        
    if not head and res:
        return
    elif head and not res:
        return
    
    return True


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n,m = list(map(int, input().strip().split()))
        nodes = list(map(int, input().strip().split()))
        aarb = list(map(int, input().strip().split()))
        ll=LinkedList()
        ll.head=Node(nodes[0])
        tail=ll.head
        
        for x in nodes[1:]:
            tail=insert(tail,x)
        
        for i in range(0,len(aarb),2):
            setarb(ll.head,aarb[i],aarb[i+1])
        
        res=copyList(ll.head)
        if validation(ll.head,res):
            print(1)
        else:
            print(0)
# } Driver Code Ends