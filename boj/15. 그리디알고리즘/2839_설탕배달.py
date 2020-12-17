n = int(input())

# k = n//5
# res = -1

# 5x+3y=n꼴
# while k >= 0:
# 	y = (n - 5*k) // 3
	
# 	if 5*k + 3*y == n:
# 		res = k + y
# 		break
# 	k -= 1

# print(res)

# 2번째
# 5로 나누어 떨어지는지 확인 -> 떨어지면 종료
# 3씩 빼가며 확인 반복
res = 0

while True:
	if n % 5 == 0:
		res += n//5
		break
	n -= 3
	res += 1
	if n < 0:
		res = -1
		break
print(res)