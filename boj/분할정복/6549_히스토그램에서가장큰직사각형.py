from collections import deque
import sys
input = sys.stdin.readline

while True:
	li = list(map(int, input().split()))
	
	if li[0] == 0:
		break
	
	height = li[1:]
	n = len(height)
	
	maxarea = 0
	st = deque()
	i = 0
	
	while i < n:
		while st and height[i] < height[st[-1]]: # 스택 최상단 인덱스의 높이보다 현재 인덱스 높이가 낮으면 스택 pop 후 넓이 계산
			before = st.pop()
			if st: # 스택에 값 남아있으면
				area = (i - st[-1] - 1) * height[before] # 스택 최상단 인덱스까지(가로) * pop한 높이
			else: # 스택 유일 원소였으면
				area = i * height[before] # 현재 인덱스 * pop한 높이
			maxarea = max(maxarea, area)
		st.append(i)
		i += 1
	
	while st: # 스택에 값 남아있으면 빌 떄까지 넓이 계산
		before = st.pop()
		if st:
			area = (i - st[-1] -1) * height[before]
		else:
			area = i * height[before]
		maxarea = max(maxarea, area)

	print(maxarea)

# 세그먼트 트리는 시간초과 발생 -> 스택 사용
# 1725번보다 시간, 메모리 제한 한정적