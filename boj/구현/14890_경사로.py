# import numpy # 백준은 넘파이 지원 안 해줌
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
graph = []

for _ in range(n):
	graph.append(list(map(int, input().split())))

cnt = 0

# tgraph = numpy.transpose(graph)

for c in range(n):
	check = [0] * n
	
	flag = True
	
	mk = False
	mc = 0
	
	bp = graph[0][c]
	bc = 1
	
	for i in range(n):
		x = graph[i][c]

		if i == 0:
			continue
		
		if mk:
			if np == x:
				mc += 1
				if mc == l:
					for j in range(i-l+1,i+1):
						check[j] += 1
					
					mk = False
					bp = np
					bc = 0
					mc = 0
				continue
			else:
				flag = False
				break
			
		np = x
		
		if bp == np:
			bc += 1
		elif np - bp == 1:
			if bc < l:
				flag = False
				break
			for j in range(i-l,i):
				check[j] += 1
			bp = np
			bc = 1
		elif bp - np == 1:
			if l == 1:
				check[i] += 1
				bp = np
				bc = 1
			else:
				mk = True
				mc += 1
		else:
			flag = False
			break
		
	if not mk and flag:
		for x in check:
			if x > 1:
				cnt -= 1
				break
		cnt += 1
	

for g in graph:
	check = [0] * n
	
	flag = True
	
	mk = False
	mc = 0
	
	bp = g[0]
	bc = 1
	
	for i,x in enumerate(g):
		if i == 0:
			continue
		
		if mk:
			if np == x:
				mc += 1
				if mc == l:
					for j in range(i-l+1,i+1):
						check[j] += 1
					
					mk = False
					bp = np
					bc = 0
					mc = 0
				continue
			else:
				flag = False
				break
			
		np = x
		
		if bp == np:
			bc += 1
		elif np - bp == 1:
			if bc < l:
				flag = False
				break
			
			for j in range(i-l,i):
				check[j] += 1
			
			bp = np
			bc = 1
		elif bp - np == 1:
			if l == 1:
				check[i] += 1
				bp = np
				bc = 1
			else:
				mk = True
				mc += 1
		else:
			flag = False
			break
	
	if not mk and flag:
		for x in check:
			if x > 1:
				cnt -= 1
				break
		cnt += 1
			
print(cnt)