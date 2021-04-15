import heapq

s = input().upper()

sset = list(set(s))

q = []

for x in sset:
	heapq.heappush(q, (-s.count(x), x))

resN, res = heapq.heappop(q)

if q:
	tmp, _ = heapq.heappop(q)
	if tmp == resN:
		print('?')
		quit()

print(res)