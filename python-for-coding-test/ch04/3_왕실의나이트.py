now = input()
# 1 ~ 8
x = ord(now[0]) - ord('a') + 1 # 아스키코드로 변환하여 정수형으로 맞춰줌
y = int(now[1])

steps = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [-1,2], [1,-2], [-1,-2]]

cnt = 0

for step in steps :
	nx = x + step[0]
	ny = y + step[1]
	
	if nx < 1 or nx > 8 or ny < 1 or ny >8 :
		continue
	cnt += 1
	
print(cnt)