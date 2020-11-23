def solution(a, b):
    if a == b :
        return a
        
    if a>b :
        a, b = b, a

    ans = 0
    for i in range(a, b+1) :
        ans += i
    return ans