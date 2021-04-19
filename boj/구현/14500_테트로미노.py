import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
res = 0

for _ in range(n):
	graph.append(list(map(int, input().split())))

shapes = [[[0,0],[0,1],[0,2],[0,3]], [[0,0],[1,0],[2,0],[3,0]], # - 
		[[0,0],[0,1],[1,0],[1,1]], # ㅁ
		[[0,0],[1,0],[2,0],[2,1]], [[0,0],[1,0],[1,-1],[1,-2]], [[0,0],[0,1],[1,1],[2,1]], [[0,0],[0,1],[0,2],[1,0]], # L 
		[[0,0],[0,1],[-1,1],[-2,1]], [[0,0],[1,0],[1,1],[1,2]], [[0,0],[0,1],[1,0],[2,0]], [[0,0],[0,1],[0,2],[1,2]], # L 반전
		[[0,0],[1,0],[1,1],[2,1]], [[0,0],[0,1],[-1,1],[-1,2]], # ㄴㄱ
		[[0,0],[-1,0],[-1,1],[-2,1]], [[0,0],[0,1],[1,1],[1,2]], # ㄴㄱ 반전
		[[0,0],[0,1],[0,2],[1,1]], [[0,0],[1,0],[2,0],[1,1]], [[0,0],[0,1],[0,2],[-1,1]], [[0,0],[0,1],[-1,1],[1,1]]] # ㅗ
		
def check(sx,sy,shape):
	global res
	tot = 0
	for x, y in shape:
		nx = sx + x
		ny = sy + y
		if 0 <= nx < n and 0 <= ny < m:
			tot += graph[nx][ny]
		else:
			return
	res = max(res,tot)
		

for shape in shapes:
	for i in range(n):
		for j in range(m):
			check(i,j,shape)

print(res)