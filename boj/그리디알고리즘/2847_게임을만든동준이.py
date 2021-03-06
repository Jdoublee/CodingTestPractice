n = int(input())

points = []
cnt = 0

for _ in range(n):
	points.append(int(input()))

for i in range(n-1, 0, -1): # 뒤에부터 검사
	if points[i-1] >= points[i]:
		cnt += points[i-1] - points[i] + 1
		points[i-1] = points[i]-1
	
print(cnt)