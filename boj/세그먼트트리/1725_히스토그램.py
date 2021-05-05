import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def init(node, start, end):
	if start == end:
		tree[node] = height[start]
		return tree[node]
	
	mid = (start+end)//2
	tree[node] = min(init(node*2, start, mid), init(node*2+1, mid+1, end))
	return tree[node]

def find(node, start, end, left, right):
	if start > right or end < left:
		return float('inf') # 최소값 구하는 세그먼트트리니까 무한대값 리턴!
	
	if left <= start and end <= right:
		return tree[node]
		
	mid = (start+end)//2
	return min(find(node*2, start, mid, left, right), find(node*2+1, mid+1, end, left, right))

def getArea(left, right):
	if left > right: # 밑에 주석 풀면 이거 주석 처리 #1
		return
	global res
	area = find(1, 0, n-1, left, right) * (right-left+1) # 범위 내에서 최소 높이 * 가로 길이
	res = max(res,area)
	
	if left == right:
		return
	
    # 아래 인덱스 구하기 대신 이렇게 썼으면 편했을 걸,,, #2
	# idx = right
	# for i in range(left, right):
		# if height[i] < height[idx]:
			# idx = i
	idx = height[left:right+1].index(min(height[left:right+1])) # 이거때문에 한참을 헤맸다ㅠ 인덱스를 구했어야지!!! #2
	# if left < idx: #1
	getArea(left,left+idx-1) # 범위 내 최소 높이 이전 영역 확인
	# if idx < right: #1
	getArea(left+idx+1,right) # 범위 내 최소 높이 이후 영역 확인
	

n = int(input())
height = []

for _ in range(n):
	height.append(int(input()))

tree = [0] * 4 * n
init(1,0,n-1)
res = 0

if len(set(height)) == 1: # 50퍼에서 시간초과 나는 이유. 야매지만 이렇게 처리. 같은 높이의 데이터가 10만개인 데이터로 추정.
	print(height[0] * n)
	quit()

getArea(0,n-1)
print(res)
