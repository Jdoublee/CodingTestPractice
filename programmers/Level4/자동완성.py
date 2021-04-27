def check(a,b): # a 기준으로 주변 문자열과 동일한 앞부분 찾아주는 함수
    res = ''
    i = -1
    flag = True
    
    for x,y in zip(a,b):
        i += 1
        res += x
        if x != y:
            flag = False
            break
            
    if flag and len(a) > len(b) and len(b) == i+1: # 겹치는 앞부분 다음 문자 추가 
        res += a[i+1]
        
    return res
    
    
def solution(words):
    answer = 0
    
    words.sort() # 정렬 후 앞 뒤 문자열과 비교 진행
        
    for i in range(len(words)):
        if i == 0:
            answer += len(check(words[i],words[i+1]))
        elif i == len(words)-1:
            answer += len(check(words[i],words[i-1]))
        else:
            first = len(check(words[i],words[i-1]))
            second = len(check(words[i],words[i+1]))
            answer += max(first,second)

    return answer