# Returns factorial
facts = [1]
def factorial(n):
    global facts
    for i in range(1,n+1):
        facts.append(i*facts[i-1])
factorial(int(1e6))

# def get_permutations(l, r, n):
#     even = odd = (r-l+1)//2
#     if (r-l+1)%2 != 0:
#         if l%2==0:
#             even += 1
#         else:
#             odd += 1
#     print(facts[10])
#     summ = 0
#     for p in range(n//2 + 1):
#         summ += odd**(2*p)*even**(n-(2*p))
#     return int(summ)

# l, r = map(int, input().strip().split())
# n = int(input())
# print(get_permutations(l, r, n) % (1e9+7))