from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	n, m = map(int, input().split())
	
	dcu = deque(list(map(int, input().split())))
	idx = deque([i for i in range(n)])
	cnt = 0
	
	while dcu:
		now = dcu.popleft()
		nidx = idx.popleft()
		
		if not dcu or now >= max(dcu):
			cnt += 1
			if nidx == m:
				print(cnt)
				break
		else:
			dcu.append(now)
			idx.append(nidx)
	
	