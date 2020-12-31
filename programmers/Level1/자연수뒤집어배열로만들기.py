def solution(n):
    answer = []
    n = str(n)

    for i in range(len(n)-1, -1, -1): # for문 역순으로. 두번째 인자는 열린 구간이므로 +-1한 값 넣어주기 
        answer.append(int(n[i]))
    
    return answer