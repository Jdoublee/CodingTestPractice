m = int(input())
n = int(input())

res = []
for i in range(m, n+1):
	if i**0.5 == int(i**0.5):
		res.append(i)

if res:
	print(sum(res))
	print(res[0])
else:
	print(-1)