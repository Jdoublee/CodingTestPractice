def solution(record):
    answer = []
    
    idname = {} # dic 형태로 uid:uname 저장. 리스트 두개 선언 후 index 함수 실행시 시간초과.... 딕셔너리를 애용하자 
    
    for rec in record:
        now = rec.split()
        
        if now[1] in idname.keys():
            if now[0] == 'Enter' or now[0] == 'Change':
                idname[now[1]] = now[2]
        else:
            idname[now[1]] = now[2]
            
    for rec in record:
        now = rec.split()

        if now[0] == 'Enter':
            answer.append(idname[now[1]] + '님이 들어왔습니다.')
        elif now[0] == 'Leave':
            answer.append(idname[now[1]] + '님이 나갔습니다.')
    
    return answer