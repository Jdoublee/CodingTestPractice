import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split()) # rstrip과 함께 씁시다

a = []
for _ in range(n):
    row = list(map(int, list(input().rstrip()))) # 문자열(string)을 리스트로 바꾸면 문자(char) 별로 쪼개서 저장됨. 각각의 문자를 다시 int 로 변환하여 리스트에 저장.
    a.append(row)

b = []
for _ in range(n):
    row = list(map(int, list(input().rstrip())))
    b.append(row)

cnt = 0

def reverse(i, j):
    if a[i][j] == 0:
        a[i][j] = 1
    else:
        a[i][j] = 0

for i in range(n):
    for j in range(m):
        if a[i][j] == b[i][j] or n - i < 3 or m - j < 3:
            continue

        for r in range(i, i+3):
            for c in range(j, j+3):
                reverse(r, c)
        cnt += 1

if a != b:
    cnt = -1
print(cnt)