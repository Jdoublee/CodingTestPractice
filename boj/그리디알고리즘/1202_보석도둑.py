# 우선순위 큐 사용
# 일반 배열 사용시 시간초과
# 각각의 리스트 우선순위 큐(heapq)로 선언 및 사용
import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

q = [] 
for _ in range(n):
	mv = list(map(int, input().rstrip().split()))
	heapq.heappush(q, mv) # 무게 가벼운 순으로 저장

bags = []
for _ in range(k):
	heapq.heappush(bags, int(input().rstrip())) # 무게 가벼운 순으로 저장 (최소힙)
	
res = 0
candidates = [] # 우선순위 큐. 무게 만족하는 후보 리스트.

for _ in range(k):
	w = heapq.heappop(bags) # 현재 가방의 수용 가능 최대 무게 pop
	
	while q and q[0][0] <= w:
		_, v = heapq.heappop(q) # 가격만 사용할 것
		heapq.heappush(candidates, -v) # 최대힙 (-)
	
	if candidates: # 후보군 존재하면 제일 비싼 보석 담아줌
		res -= heapq.heappop(candidates) # 양수로 더해주기 위해 - 곱해줌
	elif not q: # 후보도 없고 남은 보석 정보도 없으면 탈출
		break

print(res)