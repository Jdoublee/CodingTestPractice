import sys
input = sys.stdin.readline # 이거 쓰고 안 쓰고 차이가 10배 차이 (4356ms -> 416ms)

n = int(input())
times = []
for _ in range(n):
	times.append(list(map(int,input().split())))

times.sort(key=lambda t : (t[1], t[0])) # 끝나는 시간 기준 정렬, 같으면 먼저 시작하는게 먼저 오도록

ended = 0
cnt = 0
for time in times:
	if ended <= time[0]:
		cnt += 1
		ended = time[1]

print(cnt)