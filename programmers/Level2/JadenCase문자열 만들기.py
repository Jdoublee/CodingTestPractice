# s.split() 하면 안 됨 -> 공백문자가 맨 앞, 맨 뒤, 또는 여러 개 연속으로 나오는 경우 존재하므로~
def solution(s):
    answer = ''
    isblank = True # bool 로 공백 체크해줌
    
    for x in s:
        if x == ' ':
            isblank = True
            answer += x
        elif isblank:
            answer += x.upper()
            isblank = False
        else:
            answer += x.lower()
            
    return answer