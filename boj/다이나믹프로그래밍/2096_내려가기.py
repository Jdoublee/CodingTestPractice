import sys
input = sys.stdin.readline

n = int(input())

a, b, c = map(int, input().split())
dp1 = [a,a,0]
dp2 = [b,b,0]
dp3 = [c,c,0]

for i in range(1,n):
	a, b, c = map(int, input().split())
	
	dp1[2] = a + max(dp1[0], dp2[0])
	dp2[2] = b + max(dp1[0], dp2[0], dp3[0])
	dp3[2] = c + max(dp2[0], dp3[0])
	
	dp1[0] = dp1[2]
	dp2[0] = dp2[2]
	dp3[0] = dp3[2]
	
	dp1[2] = a + min(dp1[1], dp2[1])
	dp2[2] = b + min(dp1[1], dp2[1], dp3[1])
	dp3[2] = c + min(dp2[1], dp3[1])
	
	dp1[1] = dp1[2]
	dp2[1] = dp2[2]
	dp3[1] = dp3[2]
	

print(max(dp1[0],dp2[0],dp3[0]), min(dp1[1],dp2[1],dp3[1]))