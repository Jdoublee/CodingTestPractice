import sys
input = sys.stdin.readline

def preorder(x):
	if x == '.':
		return
	print(x, end='')
	preorder(tree[x][0])
	preorder(tree[x][1])

def inorder(x):
	if x == '.':
		return
	inorder(tree[x][0])
	print(x, end='')
	inorder(tree[x][1])

def postorder(x):
	if x == '.':
		return
	postorder(tree[x][0])
	postorder(tree[x][1])
	print(x, end='')


n = int(input())

tree = dict()

for _ in range(n):
	a, b, c = input().rstrip().split()
	tree[a] = (b, c)

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()