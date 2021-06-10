import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

res = n

for x in a:
	if x - b > 0:
		res += (x-b)//c
		if (x-b)%c>0:
			res += 1

print(res)