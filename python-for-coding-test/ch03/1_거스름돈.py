change = [500, 100, 50, 10]

n = 1260 # 입력

res = 0

for c in change :
	res += n //c
	n %= c

print(res)