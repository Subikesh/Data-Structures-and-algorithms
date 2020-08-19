def check_sum(arra, pair_sum):
    arra.sort()
    l = 0
    r = len(arra)-1
    while(l<r):
        sum = arra[l] + arra[r]
        if sum == pair_sum:
            return True
        elif sum < pair_sum:
            l+=1
        else:
            r-=1
    return False

arra = list(map(int, input().split()))
sum = int(input())
print("Sum is present" if check_sum(arra, sum) else "Sum is not present")