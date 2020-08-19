def find_missing(array):
    n = len(array)
    ar_sum = (n+1)*(n+2)//2
    current_sum = sum(array)
    lost_number = ar_sum - current_sum
    return lost_number
    
array = list(map(int, input().split()))
lost_number = find_missing(array)
print(lost_number)