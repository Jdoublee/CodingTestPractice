import sys
from collections import Counter

n = int(sys.stdin.readline()) # input() 으로 입력받으면 시간초과.
li = []
for i in range(n):
	li.append(int(sys.stdin.readline()))
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
print(round(sum(li)/n))
# 둘째 줄에는 중앙값을 출력한다.
li.sort()
print(li[n//2])
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
cnt = Counter(li)
if len(li) == 1:
	print(li[0])
else:
	a,b = cnt.most_common(2)
	if a[1]==b[1]:
		print(b[0])
	else:
		print(a[0])
# 넷째 줄에는 범위를 출력한다.
print(li[-1]-li[0])