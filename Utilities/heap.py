''' 
Priority Queue implementation using binary heaps 
https://www.youtube.com/watch?v=eVq8CmoC1x8&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=17

This code is done without using reverse mapping - takes O(n) time for remove_elem(elem)
Can be improved by implementing it - https://www.youtube.com/watch?v=eVq8CmoC1x8&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=17
'''

class BinaryHeap:
    
    # Initializing binary heap
    # Construct a priority queue using heapify in O(n) time, a great explanation can be found at:
    # http://www.cs.umd.edu/~meesh/351/mount/lectures/lect14-heapsort-analysis-part.pdf
    def __init__(self, elems = []):
        self.heap = elems
        self.heapsize = len(elems)

        # Heapify process
        for i in range(max(0, self.heapsize //2 -1), -1, -1):
            self.sink(i)

    # Returns true/false depending on if the priority queue is empty
    def is_empty(self):
        return len(self.heap) == 0

    # Clears everything inside the heap, O(n)
    def clear(self):
        self.heap = []
        self.heapsize = 0

    # Return the size of the heap
    def size(self):
        return self.heapsize

    # Returns the value of the element with the lowest
    # priority in this priority queue. If the priority
    # queue is empty null is returned.
    def peek(self):
        if self.is_empty(): return None
        return self.heap[0]

    # Removes the root of the heap, O(log(n))
    def pool(self):
        return self.remove_at(0)

    # Test if an element is in heap, O(n)
    def contains(self, elem):
        return self.heap.index(elem) != -1
  
    # Adds an element to the priority queue, the
    # element must not be null, O(log(n))
    def add(self, elem):
        if elem == None:
            raise ValueError("Null cant be added")
        self.heap.append(elem)
        self.heapsize += 1
        self.swim(self.heapsize-1)

    # Perform bottom up node swim, O(log(n))
    def swim(self, ind):
        # parent of heap 0 indexed
        parent = (ind-1)//2

        while(ind > 0 and self.heap[ind] < self.heap[parent]):
            self.heap[ind], self.heap[parent] = self.heap[parent], self.heap[ind]

            ind = parent
            parent = (ind-1)//2

    # Top down node sink, O(log(n))
    def sink(self, ind):
        left = ind * 2 + 1
        right = ind * 2 + 2
        small = left
        while True:
            if right < self.heapsize and self.heap[right] < self.heap[left]:
                small = right
            
            # check if child is out of heap bounds or we cant sink anymore
            if left < self.heapsize and self.heap[ind] < self.heap[small]:
                break
                
            # sinking one step 
            self.heap[ind], self.heap[small] = self.heap[small], self.heap[ind]
            ind = small


    # Removes a particular element in the heap, O(n)
    def remove_elem(self, elem):
        # Linear searching for elem O(n)
        i = self.heap.index(elem)
        return self.remove_at(i)

    # Removes a node at particular index, O(log(n))
    def remove_at(self, ind):
        if ind > self.heapsize: return -1
        last_index = self.heapsize - 1
        
        # Swap ind value with last index and delete last index
        self.heap[ind], self.heap[last_index] = self.heap[last_index], self.heap[ind]
        removed_data = self.heap.pop()

        # If we must delete last element
        if ind == last_index: return removed_data

        # Try swimming to top
        self.swim(ind)
        # If no changes in swim, do sink
        if ind == self.heap[ind]: self.sink(ind)
        return removed_data    

    # Recursively checks if this heap is a min heap
    # This method is just for testing purposes to make
    # sure the heap invariant is still being maintained
    # Called this method with k=0 to start at the root
    def is_min_heap(self, ind):
        left = 2 * ind + 1
        right = 2 * ind + 2

        if left < self.heapsize and self.heap[left] < self.heap[ind]: return False
        if right < self.heapsize and self.heap[right] < self.heap[ind]: return False

        return self.is_min_heap(left) and self.is_min_heap(right)

