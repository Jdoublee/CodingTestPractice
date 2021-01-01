def solution(n, m):
    answer = []
    
    # 최대공약수
    for i in range(min(n,m)+1, 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
        
    # 최소공배수
    for j in range(max(n,m), max(n,m) * min(n,m) + 1):
        if j % n == 0 and j % m == 0:
            answer.append(j)
            break
    
    return answer