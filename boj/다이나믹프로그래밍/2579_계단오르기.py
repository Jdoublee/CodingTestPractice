import sys
input = sys.stdin.readline

n = int(input())
stairs = []

for _ in range(n):
	stairs.append(int(input()))

if n < 3: # 계단 1개 혹은 2개인 경우는 다 포함해서 출력하고 종료
	print(sum(stairs))
	quit()

dp = [0] * n # 현재 인덱스 해당하는 계단은 무조건 밟을 때의 최대 점수 저장. 마지막 계단 무조건 밟아야하므로 dp[-1] 출력하기

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

for i in range(3,n):
	dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i]) # oxo'o' 또는 _ox'o'

print(dp[-1])