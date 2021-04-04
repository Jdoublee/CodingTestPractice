import sys
input = sys.stdin.readline
	
n = int(input())
graph = []

white = 0
blue = 0

for _ in range(n):
	graph.append(list(map(int, input().rstrip().split())))

def cutting(x,y,n): # 시작 위치의 좌표와 길이(크기) 인자로 받아옴
	global white, blue
	start = graph[x][y]
	
	for i in range(x,x+n):
		for j in range(y,y+n):
			if start != graph[i][j]: # 시작 위치의 색과 다르면 똑같은 크기의 네 개의 색종이로 나눈다
				cutting(x,y,n//2)
				cutting(x+n//2,y,n//2)
				cutting(x,y+n//2,n//2)
				cutting(x+n//2,y+n//2,n//2)
				return
	
	if start == 0:
		white += 1
	else:
		blue += 1
	
cutting(0,0,n)

print(white)
print(blue)
