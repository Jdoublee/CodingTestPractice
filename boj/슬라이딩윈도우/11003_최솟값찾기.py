from collections import deque
import sys
input = sys.stdin.readline

n, l = map(int,input().split())
a = list(map(int, input().split()))

dq = deque()

for i in range(n):
	while dq and dq[-1][1] > a[i]: # 현재 원소보다 큰 값 삭제
		dq.pop()
	
	while dq and dq[0][0] < i-l+1: # 범위 해당되지 않는 원소 삭제
		dq.popleft()
	
	dq.append((i,a[i]))
	
	print(dq[0][1], end=' ')