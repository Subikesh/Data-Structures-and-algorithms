""" 
Asked in Google online challenge 2020
TODO: return max(maximum range of increasing subsequence of prime numbers in minarr, maxarr)
if a number is not prime, change it to nearest prime less or greater than that number and find the LIS

1<= N <=1000
1<= Ai <= 10^6

Example:
8, 7, 19, 1, 2
O/P: 2 
Explanation:
2 - [1, 2] is the LIS

7, 20, 12, 12, 15, 19
O/P: 5
Explanation:
[7, 11, 13, 17, 19] is the LIS. 
Here first 12 is changed to 11 and second 12 is changed to 13.
15 -> 17 
"""

# Function returns all the primes from 1 to n
def get_primes(N):
    primes = [True for _ in range(N+1)]
    i = 2
    while i*i <= N:
        if not primes[i]:
            # If i is not a prime number
            i += 1
            continue
        for j in range(i*i, N+1, i):
            primes[j] = False
        i += 1
    return primes

# Get min and max prime
def nearest_prime(N, primes, is_min= True):
    i = N
    while i > 1 or i < len(primes):
        if primes[i]:   
            return i
        if is_min:      i -= 1
        else:           i += 1

# To find the longest increasing sub-sequence
def LIS(arr, n, primes):
    # Using 2D dynamic programming. 
    dp = [[0 for j in range(2)] for _ in arr]
    dp[0] = [1,1]
    min_max = list(zip([nearest_prime(i, primes) for i in arr], [nearest_prime(i, primes, False) for i in arr]))
    # Filling Dp bottom-up takes O(4n^2) ~ O(n^2)
    for i in range(1, n):
        for j in range(2):
            max_len = 0
            for k in range(i):
                for l in range(2):
                    if min_max[k][l] < min_max[i][j]:
                        max_len = max(max_len, dp[k][l])
            dp[i][j] = max_len +1
    return max(max(dp))

def solution(arr, n):
    primes = get_primes(int(1e6+4))
    return LIS(arr, n, primes)

n = int(input())
arr = list(map(int, input().strip().split()))
print(solution(arr, n))