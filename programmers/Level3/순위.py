from collections import defaultdict

def solution(n, results):
    answer = 0
    
    win = defaultdict(set) # k가 v이김
    lose = defaultdict(set) # k가 v에 짐
    
    for a,b in results:
        win[b].add(a)
        lose[a].add(b)
    
    # 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다.
    for i in range(1,n+1):
        for w in win[i]: # i 에게 진 선수들은 i가 진 선수들에게도 짐(순위 밀려남)
            lose[w].update(lose[i])
        for l in lose[i]: # i 에게 이긴 선수들은 i가 이긴 선수들에게도 이김
            win[l].update(win[i])

    # print(win)
    # print(lose)
    
    for i in range(1,n+1):
        if len(lose[i]) + len(win[i]) == n-1:
            answer += 1
    
    return answer