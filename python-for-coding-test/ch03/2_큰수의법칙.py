n, m, k = map(int, input().split())
li = list(map(int, input().split()))

# 첫번째 방법 : m의 크기가 커지면 시간초과 판정 받을 것
li.sort()
cnt = 0
res = 0
for i in range(m) :
	if cnt < k :
		res += li[n-1]
		cnt += 1
	else :
		cnt = 0
		res += li[n-2]

print(res)

# 두번째 방법
res = 0
kset = li[n-1] * k + li[n-2] # k+1개가 한 세트

res = kset * m//(k+1)
res += li[n-1] * m%(k+1)

print(res)