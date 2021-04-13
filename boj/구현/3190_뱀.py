from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

graph = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(k):
	x, y = map(int, input().split())
	graph[x-1][y-1] = 1

l = int(input())
dirs = deque()

for _ in range(l):
	x, c = input().split()
	dirs.append((int(x),c))

tails = deque()

# zero : 같은 행에서 이동. 오른쪽으로 : 1, 왼쪽으로 : 0
# one : 같은 열에서 이동. 아래로 : 1, 위로 : 0

def zero(sx,sy,d):
	global t
	
	if sx < 0 or sx >= n or sy < 0 or sy >= n:
		print(t)
		return
	
	if d == 1:
		for j in range(sy,n):
			if (sx,j) in tails:
				print(t)
				return
			
			tails.append((sx,j))
			
			if graph[sx][j] == 1:
				graph[sx][j] = 0
			else:
				tails.popleft()
			
			if dirs and t == dirs[0][0]:
				t += 1
				x, c = dirs.popleft()
				if c == 'L':
					one(sx-1,j,0)
				else:
					one(sx+1,j,1)
				return
			
			t += 1
	else:
		for j in range(sy,-1,-1):
			if (sx,j) in tails:
				print(t)
				return
			
			tails.append((sx,j))
			
			if graph[sx][j] == 1:
				graph[sx][j] = 0
			else:
				tails.popleft()
			
			if dirs and t == dirs[0][0]:
				t += 1
				x, c = dirs.popleft()
				if c == 'L':
					one(sx+1,j,1)
				else:
					one(sx-1,j,0)
				return
					
			t += 1

	print(t)
	return

# zero : 같은 행에서 이동. 오른쪽으로 : 1, 왼쪽으로 : 0
# one : 같은 열에서 이동. 아래로 : 1, 위로 : 0

def one(sx,sy,d):
	global t
	
	if sx < 0 or sx >= n or sy < 0 or sy >= n:
		print(t)
		return
	
	if d == 1:
		for i in range(sx,n):
			if (i,sy) in tails:
				print(t)
				return
			
			tails.append((i,sy))
			
			if graph[i][sy] == 1:
				graph[i][sy] = 0
			else:
				tails.popleft()
			
			if dirs and t == dirs[0][0]:
				t += 1
				x, c = dirs.popleft()
				if c == 'L':
					zero(i,sy+1,1)
				else:
					zero(i,sy-1,0)
				return
			t += 1

	else:
		for i in range(sx,-1,-1):
			if (i,sy) in tails:
				print(t)
				return
			
			tails.append((i,sy))
			
			if graph[i][sy] == 1:
				graph[i][sy] = 0
			else:
				tails.popleft()
			
			if dirs and t == dirs[0][0]:
				t += 1
				x, c = dirs.popleft()
				if c == 'L':
					zero(i,sy-1,0)
				else:
					zero(i,sy+1,1)
				return
			
			t += 1

	print(t)
	return

t = 0
tails.append((-1,-1)) # 길이 1부터 시작이므로 처음 값 넣어줌 
zero(0,0,1)

# 구현 문제는 조건 만족하는지, 실수/오타 없는지 확인 잘 하기