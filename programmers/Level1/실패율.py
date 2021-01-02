def solution(N, stages):
    answer = []
    
    usercnt = [0] # 1 ~ N+1
    
    for i in range(1, N+2):
        usercnt.append(stages.count(i))
    
    fails = []
    
    for i in range(1, N+1): # 마지막 단계 카운트 X
        if sum(usercnt[i:]) == 0:
            fails.append((0, -1*i))
        else:
            fails.append(((usercnt[i]/sum(usercnt[i:])), -1 * i))
            
    fails.sort(key=lambda f : (f[0], f[1]), reverse=True) # 첫번째 인자(실패율)가 같으면 index 작은 값 먼저(-1 곱해서 역순으로 해줌)
    
    answer = [-1 * f for _, f in fails]
    
    return answer