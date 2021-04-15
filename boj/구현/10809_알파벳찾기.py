s = input()

res = [-1] * 26

for i, x in enumerate(s):
	if res[ord(x)-ord('a')] < 0:
		res[ord(x)-ord('a')] = i

for x in res:
	print(x, end=' ')