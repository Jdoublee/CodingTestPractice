d = [0] * 100

def fib(x) :
    if x == 1 or x == 2 :
        return 1
    if d[x] != 0 :
        return d[x]
    d[x] = fib(x-1) + fib(x-2)
    return d[x]

print(fib(99))

# 재귀, 탑다운(메모이제이션)