def solution(d, budget):
    answer = 0
    
    d.sort()
    
    for dep in d:
        if dep <= budget:
            answer += 1
            budget -= dep
    
    return answer