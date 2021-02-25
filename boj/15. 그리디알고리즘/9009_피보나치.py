import sys
input = sys.stdin.readline

t = int(input())
fib = [0, 1]

for _ in range(t):
	n = int(input())
	res = []
	
	while fib[-1] < n:
		fib.append(fib[-1] + fib[-2])
	
	for i in range(len(fib)-1, 0, -1):
		if fib[i] <= n:
			res.append(fib[i])
			n -= fib[i]
			
			if n == 0:
				break
	res.reverse()
	for r in res:
		print(r, end=' ')
	print()