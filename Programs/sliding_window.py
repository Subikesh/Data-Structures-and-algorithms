arr = list(map(int, input().strip().split()))
k = int(input())
lower, upper = map(int, input().strip().split())
window_sum = sum(arr[i] for i in range(k))
points = 0
if window_sum < lower:
    points -= 1
if window_sum > upper:
    points += 1
for i in range(k, len(arr)):
    window_sum = window_sum + arr[i] - arr[i-k]
    if window_sum < lower:
        points -= 1
    if window_sum > upper:
        points += 1
print (points)