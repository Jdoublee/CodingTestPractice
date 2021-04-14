n = int(input())

t = 0
nn = -1
i = 0

while nn != n:
	if i == 0:
		nn = n
		i += 1
	
    first = nn//10 + nn%10
	nn = nn%10*10 + first%10

	t += 1

print(t)
# 문제 잘 읽기