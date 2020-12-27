n, m = map(int, input().split())

if n < 2:
	res = 1
elif n < 3:
	res = (m - 1) // 2 + 1
	if res > 4:
		res = 4
else:
	res = m
	if m > 4:
		if m < 7:
			res = 4 # 5, 6 일 때 4가지 다 이동 불가능.
		else:
			res -= 2
print(res)