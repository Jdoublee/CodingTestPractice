# def calc(num):
#     cnt = 0
#     for i in range(1, int(num**0.5)+1):
#         if num % i == 0:
#             cnt += 1
#     cnt *= 2
#     if int(num**0.5)**2 == num:
#         cnt -= 1
#     return cnt


def solution(left, right):
    answer = 0
    
    for x in range(left,right+1):
        if int(x**0.5) == x**0.5:
            answer -= x
        else:
            answer += x
    
    return answer