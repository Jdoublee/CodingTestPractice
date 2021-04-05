n = int(input())

graph = []

for _ in range(n):
	graph.append(list(map(int,input().split())))

none = 0
zero = 0
pone = 0

def check(x,y,n):
	global none,zero,pone
	start = graph[x][y]
	
	for i in range(x,x+n):
		for j in range(y,y+n):
			if start != graph[i][j]:
				check(x,y,n//3)
				check(x,y+n//3,n//3)
				check(x,y+2*n//3,n//3)
				check(x+n//3,y,n//3)
				check(x+n//3,y+n//3,n//3)
				check(x+n//3,y+2*n//3,n//3)
				check(x+2*n//3,y,n//3)
				check(x+2*n//3,y+n//3,n//3)
				check(x+2*n//3,y+2*n//3,n//3)
				return
	
	if start == -1:
		none += 1
	elif start == 0:
		zero += 1
	else:
		pone += 1

check(0,0,n)

print(none)
print(zero)
print(pone)
