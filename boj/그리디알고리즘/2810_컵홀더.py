n = int(input())

seats = input()

cnt = seats.count('S') + seats.count('LL') + 1

if cnt > n:
	cnt = n

print(cnt)