import sys
input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))

for num in a:
	if num < x:
		print(num, end=' ')