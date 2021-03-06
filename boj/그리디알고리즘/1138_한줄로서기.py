n = int(input())
ppl = list(map(int, input().split()))

res = [0] * n
for i in range(n):
	cnt = res[:ppl[i]].count(0)

	for j in range(ppl[i], n):
		if res[j] > 0:
			continue
		if cnt == ppl[i]:
			res[j] = i+1
			break
		cnt += 1

for r in res:		
	print(r, end=' ') # 문제 출력 예시 보자 휴