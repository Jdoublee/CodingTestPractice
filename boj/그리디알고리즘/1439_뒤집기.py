string = input().rstrip()

groups = []
tmp = []
before = ''

for s in string:
	# if before == s:
	# 	tmp.append(s) # 굳이 다 append 안 해줘도 됨. 같냐 틀리냐 구분만 해주면 됨.
	# else:
    if before != s:
        groups.append(tmp)
        tmp = [s]
        before = s

groups.append(tmp)
groups.pop(0)

print(len(groups) // 2)
