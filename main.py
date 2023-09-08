def find_fibonacci(N):
	if N == 1 or N == 2:
		return 1
	return find_fibonacci(N - 1) + find_fibonacci(N - 2)

res = find_fibonacci(125)
print(res)












