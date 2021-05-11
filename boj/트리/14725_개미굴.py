from collections import deque
import sys
input = sys.stdin.readline

class Node:
	def __init__(self, key, floor=0):
		self.key = key
		self.children = {}
		self.floor = floor # 층 저장

class Trie:
	def __init__(self):
		self.head = Node(None)
	
	def insert(self, string):
		current_node = self.head
		
		for ch in string:
			if ch not in current_node.children:
				current_node.children[ch] = Node(ch, current_node.floor+1)
			current_node = current_node.children[ch]
		
	def print_structure(self):
		current_node = self.head
		now = 0
		
        # dfs 이용 -> 정렬 내림차순으로(stack)
		q = deque()
		for x in sorted(current_node.children.keys(), reverse=True):
			q.append(current_node.children[x])
		
		while q:
			current_node = q.pop()
			print('--'*(current_node.floor-1), end='')
			print(current_node.key)
		
			for x in sorted(current_node.children.keys(), reverse=True):
				q.append(current_node.children[x])
		

n = int(input())

trie = Trie()

for _ in range(n):
	li = list(input().rstrip().split())
	
	trie.insert(li[1:])
	
trie.print_structure()