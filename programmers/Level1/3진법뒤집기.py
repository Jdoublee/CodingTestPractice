def solution(n):
    ans = ''
    answer = 0
    while n>0 :
        ans += str(n%3)
        n //= 3
    
    i = len(ans) - 1
    for num in ans:
        answer += int(num) * 3**i
        i -= 1
    
    return answer