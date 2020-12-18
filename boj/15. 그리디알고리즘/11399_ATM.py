n = int(input())

time_list = list(map(int, input().split()))

res = 0
before = 0

time_list.sort()

for t in time_list:
	before += t
	res += before

print(res)