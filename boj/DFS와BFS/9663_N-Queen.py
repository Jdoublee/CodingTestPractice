n = int(input())

res = 0
rows = [0] * n # 몇 번째 행에 저장할지 index 저장

# 퀸 놓을 수 있는지 검사
def promising(x):
	for i in range(x):
        # 같은 행 X. 대각선 X. 체크해줌
		if rows[x] == rows[i] or abs(rows[x]-rows[i]) == x-i:
			return False
	return True


def dfs(x):
    # 밖에서 선언한 변수 그대로 갖다 쓰기 위해 global 선언
	global res
    # 마지막 열까지 퀸 놓았으면 res++
	if x == n:
		res += 1
		return
	
	for i in range(n):
		rows[x] = i
		# 해당 행에 놓을 수 있다면 계속 탐색 이어감
		if promising(x):
			dfs(x+1)

dfs(0) # 0번째 행부터 탐색 시작
print(res)