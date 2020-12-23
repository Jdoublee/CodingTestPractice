# import sys
# input = sys.stdin.readline # 쓰면 런타임에러가 난다,,,,

n, m = map(int, input().split())

a = []
for _ in range(n):
	all_a = input()
	li = [int(a) for a in all_a]
	a.append(li)
	
b = []
for _ in range(n):
	all_b = input()
	li = [int(b) for b in all_b]
	b.append(li)

cnt = 0
def reverse(i, j):
	if a[i][j] == 0:
		a[i][j] = 1
	else:
		a[i][j] = 0

for i in range(n):
	for j in range(m):
		if a[i][j] == b[i][j] or n - i < 3 or m - j < 3:
			continue
	
		for r in range(i, i+3):
			for c in range(j, j+3):
				reverse(r, c)
		cnt += 1

if a != b:
	cnt = -1
print(cnt)