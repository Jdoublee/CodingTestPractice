import sys
input = sys.stdin.readline # 문제 조건 잘 읽기! 없을시 시간초과 뜸

t = int(input())
for _ in range(t):
	n = int(input())
	ppl = []
	for _ in range(n):
		ppl.append(list(map(int, input().split())))
	ppl.sort()
	cnt = 1
	comp = ppl[0][1]
	for i in range(1, n):
		if ppl[i][1] < comp:
			cnt += 1
			comp = ppl[i][1]
			
	print(cnt)