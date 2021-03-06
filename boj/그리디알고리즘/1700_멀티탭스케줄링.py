import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

names = list(map(int, input().rstrip().split()))

cnts = [-1] * (k+1) # 전기용품 사용 횟수
for name in set(names):
	cnts[name] = names.count(name)

cnt = 0
uses = []

for i, name in enumerate(names):
	if name in uses: # 이미 꽂혀있는 경우
		cnts[name] -= 1
		continue
	
	if len(uses) < n: # 여유 공간 있는 경우
		uses.append(name)
		cnts[name] -= 1
	else: # 여유 공간 없음. 뽑아야 할 것 정하기
		q = []
		flag = True
		for use in uses:
			if cnts[use] == 0: # 앞으로 안 쓰일 전기용품 있으면 그거 뽑아버림
				flag = False
				u = use
				break
			heapq.heappush(q, (-1*names[i+1:].index(use), use)) # 뒤에 쓸 예정이면 언제 첫번째로 나올지 index 저장 (최대힙)
		if flag: # 다 또 쓸 전기용품이면, 제일 늦게 사용될 전기용품 뽑아버림
			_, u = heapq.heappop(q)
		uses.remove(u)
		cnt += 1
		uses.append(name)
		cnts[name] -= 1
print(cnt)
			
		## cnts 제일 적은 애들 중 나중에 쓰일 전기용품 찾았음 -> cnts 상관없이 구해줘야했음	
		# c, u = heapq.heappop(q)
		# if c == 0: # 앞으로 안 쓰이면 뽑기
		# 	uses.remove(u)
		# else: # 제일 나중에 쓰일 것 뽑기
		# 	nq = []
		# 	while True:
		# 		cc, uu = heapq.heappop(q)
		# 		if c < cc:
		# 			break
		# 		heapq.heappush(nq, (-1*names[i+1:].index(uu), uu))
		# 	heapq.heappush(nq, (-1*names[i+1:].index(u), u))
		# 	c, u = heapq.heappop(nq)
		# 	uses.remove(u)
		# cnt += 1
		# uses.append(name)
		# cnts[name] -= 1
# print(cnt)		