def solution(n):
    
#     f = [0 for _ in range(n+1)]
    
#     f[0] = 0
#     f[1] = 1
    
#     for i in range(2, n+1):
#         f[i] = f[i-2] + f[i-1]
        
#     return f[n] % 1234567
    
    a = 0
    b = 1
    
    for _ in range(2, n+1):
        a, b = b, a+b
        
    return b % 1234567
    # 이렇게 따로 값 저장 안 하고 연산만 하는 것 신박해