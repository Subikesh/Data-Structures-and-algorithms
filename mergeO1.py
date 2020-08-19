# Given two sorted arrays arr1[] and arr2[] in non-decreasing order with size n and m. The task is to merge the two sorted arrays in place, i. e., we need to consider all n + m elements in sorted order, then we need to put first n elements of these sorted in first array and remaining m elements in second array.

# Note: Expected time complexity is O((n+m) log(n+m)). DO NOT use extra space.  We need to modify existing arrays as following.

def get_gap(gap):
    if gap <= 1:
        return 0
    # getting gap to be ceil division of gap/2
    return (gap//2) + (gap%2)
    
def merge(a,n,b,m):
    #code here
    gap = get_gap(n+m)
    
    while gap > 0:
        
        # Sorting for gaps inside first array
        i = 0
        while (i + gap) < n:
            if a[i] > a[i+gap]:
                a[i], a[i+gap] = a[i+gap], a[i]
            i += 1
        
        # Sorting for gaps within two arrays
        j = gap-n if gap>n else 0
        while i<n and j<m:
            if a[i] > b[j]:
                a[i], b[j] = b[j], a[i]
            i += 1
            j += 1
        
        # Sorting for gaps in second array
        if j < m:
            j = 0
            while j+gap < m:
                if b[j] > b[j+gap]:
                    b[j], b[j+gap] = b[j+gap], b[j]
                j += 1
        
        gap = get_gap(gap)

arr1 = list(map(int, input().strip().split()))
arr2 = list(map(int, input().strip().split()))

merge(arr1, len(arr1), arr2, len(arr2))


print(arr1, arr2)