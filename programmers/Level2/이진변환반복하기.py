def solution(s):    
    cnt = 0
    zeros = 0
    
    while True:
        cnt += 1
        
        zero = s.count('0')
        
        zeros += zero
        
        s = bin(len(s) - zero)[2:]
            
        if s == '1':
            break

    return [cnt, zeros]


    # 한국말로 된 문제도 버벅이는데 영어로 어떻게 푸냐 ㄸㅎㅎ