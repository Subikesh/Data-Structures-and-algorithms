# An array A consists of n integers in locations A[0], A[1] ....A[n-1]. 
# It is required to shift the elements of the array cyclically to the left by k places, where 1 <= k <= (n-1).

def rotate(ar, k):
    n = min = len(ar)
    i = 0
    while i<min:
        temp = ar[i]
        j = i
        while j!= ((n+i-k) %n):
            ar[j] = ar[(j+k)%n]
            j = (j+k)%n
            if j<min:   min = j
            a = (n+i-k) %n
        ar[(n+i-k)%n] = temp
        i += 1
    print(ar)

ar = [0,1,2,3,4,5,6,7]
rotate(ar, 3)