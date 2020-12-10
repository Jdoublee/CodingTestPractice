n = int(input())
stock = list(map(int, input().split())) # 중복되어 있다면 set 자료형 사용

m = int(input())
order = list(map(int, input().split()))

# stock.sort()

for num in order :
    if num in stock :
        print('yes', end=' ')
    else :
        print('no', end=' ')