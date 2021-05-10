from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
node = [[] for _ in range(n)]

info = list(map(int, input().split()))
delete = int(input())

res = 0
root = -1

for i,x in enumerate(info):
	if x == -1:
		root = i
		continue
	node[x].append(i)

if delete == root: # 루트노드 삭제시 단말노드 0 종료
	print(res)
	quit()

q = deque()
for x in node[delete]:
	q.append(x)

node[delete] = []

while q: # 삭제할 노드의 자식 노드 삭제
	now = q.popleft()

	for x in node[now]:
		q.append(x)
		
	node[now] = []

node[info[delete]].remove(delete) # 삭제할 노드 본인 삭제

for i in node[root]:
	q.append(i)

while q: # 단말노드 세기
	now = q.popleft()

	if not node[now]:
		res += 1
	else:
		for x in node[now]:
			q.append(x)

if not res: # 98퍼 -> 루트노드가 단말노드인 경우
	res = 1
print(res)

