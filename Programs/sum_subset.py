def get_indices(arr, n, given_sum):
    curr_sum = arr[0]
    start = 0
    for i in range(1, n):
        while curr_sum > given_sum and start < i-1:
            curr_sum -= given_sum
            start +=1
        
        if curr_sum == given_sum:
            print(start, i-1)
            break
        
        curr_sum += arr[i]
    else:
        print(-1)

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n, s = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))
        get_indices(arr, n, s)