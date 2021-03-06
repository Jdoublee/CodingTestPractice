import sys
input = sys.stdin.readline

n, l = map(int, input().rstrip().split())

locs = list(map(int, input().rstrip().split()))

locs.sort()

cnt = 0
# start = 0
end = 0
for loc in locs:
	if end < loc:
        # start = loc - 0.5
		end = loc + l - 0.5 # end = start + l
		cnt += 1

print(cnt)