import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

res = [-1 for _ in range(n)]

st = [0] # 인덱스 저장
i = 1

while st and i < n:
	while st and a[st[-1]] < a[i]: # 큰 원소 발견 시
		res[st[-1]] = a[i] # res update
		st.pop() # st에서 삭제
	st.append(i) # 현재 인덱스의 값 st에 추가
	i += 1

for r in res:
	print(r, end=' ')
