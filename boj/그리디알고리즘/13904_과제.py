import heapq
import sys

input = sys.stdin.readline

n = int(input())

h = []

for _ in range(n):
	a, b = map(int, input().split())
	b *= -1
	h.append((b,a))
	
maxd = max(h, key=lambda x:x[1])[1]
date = [0] * (maxd+1) # 가능한 날짜 수+1 만큼 리스트 생성

heapq.heapify(h)

for _ in range(n):
	a, b = heapq.heappop(h)
	
	while b > 0:
		if date[b]: # 해당 날짜 이미 차있으면 b--
			b -= 1
		else: # 해당 날짜 비어있으면 점수 넣어주기
			date[b] = -a
			break
	
	
print(sum(date))