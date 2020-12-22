first_input = input()

nums = first_input.split('-')

res = 0

for i, num in enumerate(nums):
	now = list(map(int, num.split('+')))
	if i == 0:
		res += sum(now)
	else:
		res -= sum(now)

print(res)