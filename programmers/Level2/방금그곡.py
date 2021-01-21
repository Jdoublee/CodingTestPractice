# 27, 28, 30 틀림
#
# def solution(m, musicinfos):
#     answer = ''
    
#     res = []
    
#     for idx, music in enumerate(musicinfos):
#         start, end, title, melody = music.split(',')
        
#         tmp = []
#         for i, mld in enumerate(melody):
#             if mld == '#':
#                 before = tmp.pop()
#                 tmp.append(before+mld)
#             else:
#                 tmp.append(mld)
                
#         melody = tmp
        
#         end = int(end[:2]) * 60 + int(end[3:])
#         start = int(start[:2]) * 60 + int(start[3:])
        
#         time = end - start
#         total = len(melody)
        
#         if len(melody) < time:
#             i = 0
#             while time - len(melody) > 0:
#                 if i == total:
#                     i = 0
#                 melody.append(melody[i])
#                 i += 1
        
#         cmp = ''.join(melody)
        
#         i = 0
#         while i < len(cmp):
#             if m in cmp[i:]:
#                 vali = cmp[i:].find(m) + i
#                 if vali+len(m) == len(cmp):
#                     res.append((time, idx))
#                     i = len(cmp)
#                     break
#                 if cmp[vali+len(m)] != '#':
#                     res.append((time, idx))
                
#                 i = vali+len(m)
#             else:
#                 break
            
    
#     if res == []:
#         return "(None)"
#     res.sort(reverse=True)
#     _, idx = res.pop(0)
    
#     answer = musicinfos[idx].split(',')[2]
    
    
#     return answer


def solution(m, musicinfos):

    answer = "(None)" # 일치하는 음악 없을 경우 리턴할 값

    res = []

    for idx, music in enumerate(musicinfos):
        start, end, _, melody = music.split(',') # title 쓸 일 없어서 _ 로 받음
        
        tmp = []
        for mld in melody:
            if mld == '#':
                before = tmp.pop()
                tmp.append(before.lower()) # 위 방법과 달리 # 음을 소문자 C# -> c 처리. ~ in ~ 구문 활용하기 용이해짐.
            else:
                tmp.append(mld)
        melody = tmp # 음 하나씩 리스트로 저장
        
        tmp = []
        for ml in m:
            if ml == '#':
                before = tmp.pop()
                tmp.append(before.lower()) # 위와 똑같이 처리
            else:
                tmp.append(ml)
        m = tmp
        
        # 재생시간 계산. 시간 * 60 + 분 처리.
        e = int(end[:2]) * 60 + int(end[3:])
        s = int(start[:2]) * 60 + int(start[3:])
        
        time = e - s
        total = len(melody) # 곡 정보 주어진 악보 길이
        
        # 이 부분 수정해줘서 30 번 테케 해결
        # 재생시간이 더 긴 경우 몇 번 반복되고, 얼마나 더 붙여줘야 되는지 divmod 써서 추가
        if total == time:
            cmp = ''.join(melody)
        else:
            q, r = divmod(time, len(melody))
            cmp = ''.join(melody)
            tmp = ''.join(melody[:r])
            cmp = cmp * q + tmp
                
        song = ''.join(m)
        
        if song in cmp:
            res.append((time, -idx)) # 재생시간 긴거부터 & 인덱스는 작은 수부터여야 하므로 - 곱해서 리스트에 넣어줌. 27, 28번 테케 해결!!
            
    if not res:
        return answer

    res.sort(reverse=True)
    _, idx = res.pop(0)

    answer = musicinfos[-idx].split(',')[2]

    return answer

# 경우 다 잘 생각해보자