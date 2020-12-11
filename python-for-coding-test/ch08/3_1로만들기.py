x = int(input())

d = [0] * 30001
# d[1] = 0
for i in range(2, x+1) :
    # d - 1 빼는 경우
    d[i] = d[i-1] + 1
    # 아래부턴 나누는 연산 1회씩 더해서 비교
    # c - 2로 나누어 떨어지는 경우
    if i % 2 == 0 :
        d[i] = min(d[i], d[i//2] + 1)
    # b - 3으로 나누어 떨어지는 경우
    if i % 3 == 0 :
        d[i] = min(d[i], d[i//3] + 1)
    # a - 5로 나누어 떨어지는 경우
    if i % 5 == 0 :
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])
