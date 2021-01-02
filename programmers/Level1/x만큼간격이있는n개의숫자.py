def solution(x, n):
    answer = []
    
    for i in range(n):
        answer.append(x * (i + 1))
    
    return answer