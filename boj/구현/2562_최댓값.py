nums = []

for _ in range(9):
	nums.append(int(input()))

res = max(nums)

print(res)
print(nums.index(res)+1)