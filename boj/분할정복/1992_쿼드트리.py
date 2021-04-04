import sys
input = sys.stdin.readline

n = int(input())

graph = []

res = ''

for _ in range(n):
	graph.append(list(map(int,list(input().rstrip())))) # 띄어쓰기 없이 이어져서 입력으로 들어옴. 문자열 -> list 처리

def check(x,y,n):
	global res
	start = graph[x][y]
	
	
	for i in range(x,x+n):
		for j in range(y,y+n):
			if start != graph[i][j]:
				res += '('
				check(x,y,n//2)
				check(x,y+n//2,n//2)
				check(x+n//2,y,n//2)
				check(x+n//2,y+n//2,n//2)
				res += ')'
				return
	
	res += str(start)

check(0,0,n)

print(res)