def solution(n):    
    num = list(str(n)) # 문자열 리스트에 넣기 꿀팁
    
    num.sort(reverse=True)
    
    answer = int(''.join(num))
        
    return answer