def solution(n,a,b):
    answer = 0
    
    while True:
        answer += 1
        if (a+1)//2 == (b+1)//2: # 이진 트리 구조. 이번 라운드 이겼을 때 받을 번호 같으면 이번 라운드에 만났다는 뜻.
            break # return answer
        a = (a+1)//2
        b = (b+1)//2
    
    return answer