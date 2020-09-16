def get_longest_ones(A, k):
	left = 0
	rem = k-1
	lenn = max_len = 0
	for right in range(len(A)):
		if A[right] == 1:
			lenn += 1
		else:
			if rem >= 0:
				lenn += 1
				rem -= 1
			else:
				max_len = max(max_len, lenn)
				while A[left] == 1 and left <= right:
					left += 1
					lenn -= 1
				left += 1
				lenn -= 1
				rem += 1
	max_len = max(max_len, lenn)
	return max_len


A = list(map(int, input().strip().split()))
K = int(input())
print(get_longest_ones(A, K))