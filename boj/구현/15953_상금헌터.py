import sys
input = sys.stdin.readline

t = int(input())

m17 = [0] + [500]*1 + [300]*2 + [200]*3 + [50]*4 + [30]*5 + [10]*6
m18 = [0] + [512]*1 + [256]*2 + [128]*4 + [64]*8 + [32]*16

for _ in range(t):
	a, b = map(int, input().split())
	tot = 0
	
	if a < len(m17):
		tot += m17[a]
	
	if b < len(m18):
		tot += m18[b]
	
	print(tot*10000)
		
# 메모리, 시간은 if문 줄줄이랑 똑같지만 이렇게도 풀 수 있다.
# 2018년 본선은 2의 제곱꼴이므로 2진수 비트비트 생각