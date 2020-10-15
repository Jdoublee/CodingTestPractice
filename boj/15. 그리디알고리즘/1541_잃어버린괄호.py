# 깔쌈한 방법을 찾아야지
import re

a = input()
num = list(map(int, re.split('[+-]', a)))
op = [op for op in re.split('[0-9]', a) if op!='']

tot = num[0]
li = []
minus = False
for i,opr in enumerate(op):
	if opr=='+':
		if minus == True:
			li.append(num[i+1])
		else:
			tot += num[i+1]
	else:
		if minus == True:
			for n in li:
				tot -= n
			li = [num[i+1]]
		else:
			minus = True
			li.append(num[i+1])
if li != []:
	if minus == True:
		for n in li:
			tot -= n
	else:
		for n in li:
			tot += n
print(tot)