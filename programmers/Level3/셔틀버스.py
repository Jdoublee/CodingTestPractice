def str_int(s): # 시간 문자열 -> 정수
    h = int(s[:2])
    m = int(s[3:])
    
    return h, m


def int_str(h,m): # 시간 정수 -> 문자열
    time = ''
    if h < 10:
        time += '0'
    time += str(h)
    time += ':'
    if m < 10:
        time += '0'
    time += str(m)
    return time
    
    
def hm(m): # 분 -> 시간, 분
    h = 0
    if m > 60:
        h = m // 60
        m = m % 60
    return h, m


def solution(n, t, m, timetable):    
    lh, lm = hm(t*(n-1))
    lh += 9
    
    timetable.sort() # 도착시간 정렬 필요
    times = [str_int(t) for t in timetable]
    # times.sort(key=lambda x:(x[0],x[1]))

    # 제일 먼저 도착하는 크루 시간이 마지막 셔틀 시간보다 늦는 경우 또는 크루 수가 m보다 적은 경우
    if times[0][0] > lh or (times[0][0] == lh and times[0][1] > lm) or len(times) < m: 
        return int_str(lh,lm)
    
    sh, sm = 9, 0 # 현재 셔틀 출발 시간(첫번째부터)
    i = 0
    
    while n > 1: # 마지막 셔틀 전까지
        cnt = 0
        n -= 1
        while cnt < m and i < len(times): # 현재 셔틀에 탈 자리 남은경우
            nh, nm = times[i]
            if nh < sh or (nh == sh and nm <= sm): # 현재 셔틀 출발 시간 전에 크루 도착한 경우
                cnt += 1
                i += 1
            else:
                break
                
        sm += t # 다음 셔틀 시간으로 변경
        if sm >= 60:
            a, b = hm(sm)
            sh += a
            sm = b
            
    # 마지막 셔틀에 모두 탈 수 있는 경우
    if len(times) - i < m:
        return int_str(lh,lm)
    
    flh, flm = times[i+m-1] # 남은 크루 중 마지막 크루의 도착 시간
    
    # 마지막 크루의 도착 시간이 마지막 셔틀 시간보다 늦은 경우
    if flh > lh or (flh == lh and flm > lm): # tc18
        return int_str(lh,lm)
    # 마지막 크루 도착 시간 1분 전 반환
    if flm == 0:
        flh -= 1
        flm = 59
    else:
        flm -= 1

    return int_str(flh,flm)