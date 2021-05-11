import sys
input = sys.stdin.readline

class Node:
	def __init__(self, key):
		self.key = key
		self.data = None
		self.children = {}

class Trie:
	def __init__(self):
		self.head = Node(None) # root
	
	def insert(self, string):
		current_node = self.head
		
		for ch in string:
			if ch not in current_node.children:
				current_node.children[ch] = Node(ch)
			current_node = current_node.children[ch]
		
		current_node.data = string
	
	def search(self, string):
		current_node = self.head
		
		for ch in string:
			if current_node.data:
				return False
			current_node = current_node.children[ch]
			
		return True
			

t = int(input())

for _ in range(t):
	n = int(input())
	numbers = []
	
	trie = Trie()
	
	for _ in range(n):
		number = input().rstrip()
		numbers.append(number)
		trie.insert(number)
	
	i = 0
	res = True
	
	while i < n:
		if not trie.search(numbers[i]):
			res = False
			break
		i += 1
	
	if res:
		print('YES')
	else:
		print('NO')