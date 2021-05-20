import sys
input = sys.stdin.readline

A = list(map(int,list(input().rstrip())))
B = list(map(int,list(input().rstrip())))
C = list(map(int,list(input().rstrip())))
D = list(map(int,list(input().rstrip())))

# 12시 인덱스
ap = 0
bp = 0
cp = 0
dp = 0

k = int(input())

for _ in range(k):
	n, d = map(int, input().split()) # 회전 방향 유의
	
	if n == 1:
		if A[(ap+2)%8] != B[(bp+6)%8]:
			if B[(bp+2)%8] != C[(cp+6)%8]:
				if C[(cp+2)%8] != D[(dp+6)%8]:
					dp = (dp+8+d)%8
				cp = (cp+8-d)%8
			bp = (bp+8+d)%8
		ap = (ap+8-d)%8
	elif n == 2:
		if A[(ap+2)%8] != B[(bp+6)%8]:
			ap = (ap+8+d)%8
		if B[(bp+2)%8] != C[(cp+6)%8]:
			if C[(cp+2)%8] != D[(dp+6)%8]:
				dp = (dp+8-d)%8
			cp = (cp+8+d)%8
		bp = (bp+8-d)%8
	elif n == 3:
		if B[(bp+2)%8] != C[(cp+6)%8]:
			if A[(ap+2)%8] != B[(bp+6)%8]:
				ap = (ap+8-d)%8
			bp = (bp+8+d)%8
		if C[(cp+2)%8] != D[(dp+6)%8]:
			dp = (dp+8+d)%8
		cp = (cp+8-d)%8
	else:
		if C[(cp+2)%8] != D[(dp+6)%8]:
			if B[(bp+2)%8] != C[(cp+6)%8]:
				if A[(ap+2)%8] != B[(bp+6)%8]:
					ap = (ap+8+d)%8
				bp = (bp+8-d)%8
			cp = (cp+8+d)%8
		dp = (dp+8-d)%8

res = 0
if A[ap]:
	res += 1
if B[bp]:
	res += 2
if C[cp]:
	res += 4
if D[dp]:
	res += 8
print(res)