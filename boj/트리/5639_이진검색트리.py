import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def postorder(start, end):
	if start >= end:
		return
	
	mid = end
	for i in range(start+1,end):
		if tree[start] < tree[i]:
			mid = i
			break
	postorder(start+1,mid)
	postorder(mid,end)
	print(tree[start])


tree = []

while True:
	try:
		now = int(input())
		tree.append(now)
	except:
		break
	
postorder(0,len(tree))	
	




## 26-27퍼 시간초과 코드 #
#
# class Node:
# 	def __init__(self, key):
# 		self.key = key
# 		self.left = None
# 		self.right = None

# class Tree:
# 	def __init__(self):
# 		self.root = None
	
# 	def insert(self, key):
# 		if not self.root:
# 			self.root = Node(key)
# 			return
		
# 		cur_node = self.root
		
# 		while True:
# 			if key < cur_node.key:
# 				if cur_node.left:
# 					cur_node = cur_node.left
# 				else:
# 					cur_node.left = Node(key)
# 					break
# 			else:
# 				if cur_node.right:
# 					cur_node = cur_node.right
# 				else:
# 					cur_node.right = Node(key)
# 					break
		
# 	def postorder(self, node=None):
# 		if node:
# 			cur_node = node
# 		else:
# 			cur_node = self.root
		
# 		if cur_node.left:
# 			self.postorder(cur_node.left)
# 		if cur_node.right:
# 			self.postorder(cur_node.right)
# 		print(cur_node.key)
# 
# 
# tree = Tree()
# 
# while True:
# 	try:
# 		now = int(input())
# 		# tree.insert(now)
# 	except:
# 		break
# 
# tree.postorder()
