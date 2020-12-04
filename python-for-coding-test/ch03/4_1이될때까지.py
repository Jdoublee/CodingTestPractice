n, k = map(int, input().split())

res = 0
while n!= 1 :
	if n % k == 0 :
		res += 1
		n /= k
	else :
		res += 1
		n -= 1
print(res)

# 이렇게 풀면 안 되나 흠냐뤼
# https://github.com/ndb796/python-for-coding-test/blob/master/3/6.py