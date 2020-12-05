n = int(input())

cnt = 0
for h in range(n+1) :
	for m in range(60) :
		for s in range(60) :
			if h%10==3 or m%10==3 or m//10==3 or s%10==3 or s//10==3 :
				cnt += 1

print(cnt)

# 답안 예시
# str 로 비교

cnt = 0
for h in range(n+1) :
	for m in range(60) :
		for s in range(60) :
			if '3' in str(h) + str(m) + str(s) :
				cnt += 1

print(cnt)
