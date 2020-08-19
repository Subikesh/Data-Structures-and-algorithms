# By using two pointer sum method to count if any 2 numbers in arr equals the given sum
def check_sum(arr, n, sum):
    l = 0
    r = n-1
    count = 0
    while l < r:
        cur_sum = arr[l] + arr[r]
        if cur_sum == sum:
            print(sum, arr[l], arr[r], end = '    ')
            count +=1
            l+=1
        elif cur_sum < sum:
            l+=1
        else:
            r-=1
        # print()
    return count

def count_triplets(arr, n):
    count = 0
    arr.sort()
    print('Triplets are :')
    for i in range(n-1, -1, -1):
        count += check_sum(arr[:i]+arr[(i+1):], n-1, arr[i])
    print('Count is', end = ' ')
    return count if count > 0 else -1

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(count_triplets(arr, n))