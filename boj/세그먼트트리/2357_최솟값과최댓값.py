import sys
input = sys.stdin.readline

def init_min(node, start, end):
	if start == end:
		tree_min[node] = nums[start]
		return tree_min[node]
		
	mid = (start+end)//2
	tree_min[node] = min(init_min(node*2, start, mid), init_min(node*2+1, mid+1, end))
	return tree_min[node]

def find_min(node, start, end, left, right):
	if left > end or right < start:
		return float('inf')
	
	if left <= start and end <= right:
		return tree_min[node]
	
	mid = (start+end)//2
	return min(find_min(node*2, start, mid, left, right), find_min(node*2+1, mid+1, end, left, right))

def init_max(node, start, end):
	if start == end:
		tree_max[node] = nums[start]
		return tree_max[node]
		
	mid = (start+end)//2
	tree_max[node] = max(init_max(node*2, start, mid), init_max(node*2+1, mid+1, end))
	return tree_max[node]

def find_max(node, start, end, left, right):
	if left > end or right < start:
		return 0
	
	if left <= start and end <= right:
		return tree_max[node]
	
	mid = (start+end)//2
	return max(find_max(node*2, start, mid, left, right), find_max(node*2+1, mid+1, end, left, right))

n, m = map(int, input().split())
nums = []

tree_min = [0] * 4 * n
tree_max = [0] * 4 * n

for _ in range(n):
	nums.append(int(input()))

init_min(1,0,n-1)
init_max(1,0,n-1)

for _ in range(m):
	a, b = map(int, input().split())
	print(find_min(1,0,n-1,a-1,b-1), find_max(1,0,n-1,a-1,b-1))