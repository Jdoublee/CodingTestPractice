def solution(n):
    m = n # 원래 입력으로 받은 n 값 저장
    s = 1 # 시작
    t = 0 # while문 몇 번 도는지
    answer = [[] for _ in range(n)]
    back = [[] for _ in range(n)] # 역으로 도는 변 값들 저장. 나중에 reverse해서 뒤에 붙여줌.
    
    res = []
    
    while s > 0:
        for i in range(n):
            answer[2*t+i].append(s+i)

        for i in range(n+1, 2*n):
            answer[2*t+n-1].append(s+i-1)
        
        k = 2
        for i in range(2*n, 3*n-2):
            back[2*t+n-k].append(s+i-1)
            k += 1
            
        s += 3*n-1 # 기존 값에 더해줘야 함!!
        n -= 3 # 위 두 줄, 아래 한 줄 씩 줄어듦.
        t += 1 # 횟수 ++

    for i in range(m):
        back[i].reverse() # 들어온 순서대로 저장되어 있으니 뒤집어서 붙여줘야 함.

    for i in range(m):
        answer[i].extend(back[i]) # extend로 연장.
    
    for ans in answer:
        res.extend(ans) # 최종 답안 res에 이어서 저장.
    
    return res