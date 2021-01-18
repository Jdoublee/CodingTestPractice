def solution(msg):
    answer = []
    
    dic = list('0ABCDEFGHIJKLMNOPQRSTUVWXYZ') # 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다. index 1부터 시작 & 대문자만 존재하므로 dic[0]=0 임의로 넣어줌.
    
    idx = 0
    flag = False # 마지막 단어 처리 위한 bool
    
    while idx < len(msg):
        w = msg[idx] # 한 글자는 사전에 이미 존재
        while w in dic: # 무조건 돈다. 돌고 나중에 맨 뒤 문자는 c로 따로 처리
            if idx == len(msg) - 1:
                flag = True
                break
            idx += 1
            w += msg[idx]
        if flag: # 마지막 단어는 사전에 추가 없이 바로 정답에 추가
        	answer.append(dic.index(w))
        	break
        w, c = w[:-1], w[-1] 
        dic.append(w+c) # 사전에 추가
        answer.append(dic.index(w)) # 현재 w 값 정답에 추가
        
    return answer