# 조건 추후에 추가하느라 길고 지저분해졌다
n = int(input())
nums = []
for _ in range(n):
	nums.append(int(input()))
# 양수 따로
pnums = [n for n in nums if n > 0]
pnums.sort(reverse=True)
# 음수 따로 (0 있는 경우 나중에 처리)
nnums = [n for n in nums if n < 0]
nnums.sort()

res = 0
before = 12345 # 범위 밖
for i in range(len(pnums)):
	if pnums[i] == 1:
		if before <= 10000: # 이전 값 존재하고, 현재 값 1이면 곱하지 않고 각각 더해줌
			res += before + 1
			before = 12345
		else:
			res += 1 # 이전 값 없다면 1만 더해줌
		continue
	if i % 2 == 0:
		before = pnums[i]
	else:
		res += before * pnums[i]
		before = 12345
if len(pnums) % 2 != 0 and before <= 10000: # 1 아니었던 값 남아있으면
	res += before

for i in range(len(nnums)):
	if i % 2 == 0:
		before = nnums[i]
	else:
		res += before * nnums[i]
		
if len(nnums) % 2 != 0 and 0 not in nums: # 0이 존재하면 음수와 0 곱해 0 이므로 처리 ㄴㄴ, 0 없으면 이전 값 처리
	res += before

print(res)
