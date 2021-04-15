n = input()

cnt = [0] * 9

for x in n:
	x = int(x)
	if x == 9:
		x = 6
	cnt[x] += 1

if max(cnt) == cnt[6]:
	cnt[6] = (cnt[6]+1) // 2

print(max(cnt))