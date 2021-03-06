n = int(input())

li = [[] for i in range(50)] # 0 ~ 49
idx = 0
for i in range(n):
	a = input()
	li[len(a)-1].append(a)
for l in li:	
	if l != []:
		l = list(set(l)) # 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
		l.sort()
		print('\n'.join(l))
