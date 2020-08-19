#User function Template for python3
def mergeArrays(a,b,n,m):
    '''
    :param a: given sorted array a
    :param n: size of sorted array a
    :param b: given sorted array b
    :param m: size of sorted array b
    :return:  The union of both arrays as a list
    '''
    # code here 
    merged = []
    elems = set()
    A = B = 0
    while A < n and B < m:
        if a[A] <= b[B]:
            if a[A] not in elems:
                merged.append(a[A])
                elems.add(a[A])
            A += 1
        elif b[B] < a[A]:
            if b[B] not in elems:
                merged.append(b[B])
                elems.add(b[B])
            B += 1

    while A < n:
        if a[A] not in elems:
            merged.append(a[A])
            elems.add(a[A])
        A += 1
    while B < m:
        if b[B] not in elems:
            merged.append(b[B])
            elems.add(b[B])
        B += 1
    return merged

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        li = mergeArrays(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends