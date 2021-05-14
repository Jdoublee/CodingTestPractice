import sys
input = sys.stdin.readline

def dfs(x):
    visited[x] = True
    
    for n in path[x]:
        if col[n] == -1 or (not visited[col[n]] and dfs(col[n])):
            row[x] = n
            col[n] = x
            return True
            
    return False


graph = []

n = int(input())

for _ in range(n):
	graph.append(list(input().rstrip()))

r = [[-1 for _ in range(n)] for _ in range(n)]
rp = 0
c = [[-1 for _ in range(n)] for _ in range(n)]
cp = 0

for i in range(n):
    flag = False
    
    for j in range(n):
        if graph[i][j] == '.': # 0
            r[i][j] = rp
            flag = True
        elif flag:
            flag = False
            rp += 1
    if flag:
        rp += 1

for j in range(n):
    flag = False
    
    for i in range(n):
        if graph[i][j] == '.':
            c[i][j] = cp
            flag = True
        elif flag:
            flag = False
            cp += 1
    if flag:
        cp += 1
        
rp += 1
cp += 1

path = [[] for _ in range(rp)]

for i in range(n):
    for j in range(n):
        if r[i][j] >= 0 and c[i][j] >= 0:
            path[r[i][j]].append(c[i][j])

row = [-1] * rp
col = [-1] * cp
res = 0

for i in range(rp):
    if row[i] == -1:
        visited = [False] * rp
        if dfs(i):
            res += 1

print(res)
