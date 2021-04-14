import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	string = list(input().rstrip())
	suc = 0
	res = 0
	
	for ch in string:
		if ch == 'O':
			suc += 1
			res += suc
		else:
			suc = 0
	
	print(res)