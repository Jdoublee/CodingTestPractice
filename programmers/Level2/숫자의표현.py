def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        tot = i
        for j in range(i+1, n+1):
            if tot >= n:
                break
            tot += j
        if tot == n:
            answer += 1
                
    return answer