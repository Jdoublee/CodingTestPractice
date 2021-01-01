def solution(num):
    cnt = 0

    while num > 1:
        if cnt >= 500:
            cnt = -1
            break

        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1

        cnt += 1
    
    return cnt