n = int(input())
money = 1000 - n
changes = [500, 100, 50, 10, 5, 1]
cnt = 0
i = 0

while money > 0:
	if changes[i] > money:
		i += 1
		continue
	cnt += money // changes[i]
	money %= changes[i]

print(cnt)