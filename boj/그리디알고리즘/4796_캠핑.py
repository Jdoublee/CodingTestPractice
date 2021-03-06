res = []
while True:
	# 캠핑장을 연속하는 P일 중, L일동안만 사용할 수 있다.
	l, p, v = map(int, input().split())
	if l == 0 and p == 0 and v == 0:
		break
	days = v // p * l
	rem = v % p
	if rem > l:
		rem = l
	days += rem
	res.append(days)

for i in range(len(res)):
	print('Case {0}: {1}'.format(i+1, res[i]))