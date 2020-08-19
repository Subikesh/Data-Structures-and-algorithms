# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.

def findMedianSortedArrays(nums1, nums2):
    '''
    nums1: shorter array
    n1:   len of arr
    nums2: larger array
    n2:   len of array
    return: median
    '''
    n = len(nums1)
    m = len(nums2)
    min_index = 0
    max_index = min(n, m)
    while True:
        i = (min_index+max_index)//2
        j = (n+m+1)//2 - i
        if i == n or j == 0 or nums2[j-1] <= nums1[i]:
            if nums1[i-1] <= nums2[j]:
                # We got the median
                if (n+m)%2 == 0:
                    if i == n:
                        right = nums2[j]
                        left = max(nums1[i-1], nums2[j-1])
                    if j == 0:
                        left = nums1[i]
                        right = min(nums1[i], nums2[j])
                    if i<n and j>0:
                        right = min(nums1[i], nums2[j])
                        left = max(nums1[i-1], nums2[j-1])
                    return (right+left)//2
                else:
                    if j == 0:
                        return nums1[i-1]
                    else:
                        return max(nums1[i-1], nums2[j-1])
            else:
                # To check left side
                max_index = i-1
        else:
            # To check right side
            min_index = i+1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n1,n2=list(map(int,(input().split())))
        arr1=list(map(int,(input().split())))
        arr2=list(map(int,(input().split())))
        
        if n1<n2:
            print(findMedianSortedArrays(arr1,n1, arr2,n2))
        else:
            print(findMedianSortedArrays(arr2,n2, arr1,n1))
# } Driver Code Ends