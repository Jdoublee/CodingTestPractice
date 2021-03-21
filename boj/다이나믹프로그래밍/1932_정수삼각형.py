n = int(input())

graph = []

for _ in range(n):
	tmp = list(map(int, input().split()))
	
	if not graph:
		graph = tmp
	else:
		res = [graph[0]+tmp[0]]

		for i in range(1, len(tmp)-1):
			res.append(max(graph[i-1], graph[i])+tmp[i])
            
		res.append(tmp[-1]+graph[-1])
		graph = res

print(max(graph))