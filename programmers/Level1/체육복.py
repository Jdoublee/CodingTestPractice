# 다른 사람 풀이 참고해보기
def solution(n, lost, reserve):
    answer = 0
    
    lst = list(set(lost) - set(reserve) )
    rsv = list(set(reserve) - set(lost))
    cnt = n - len(lst)
    
    for r in rsv:
        if r-1 in lst :
            cnt += 1
        elif r+1 in lst:
            cnt += 1
            lst.remove(r+1) # 앞뒤로 체육복 빌려준 경우 -> cnt > n 경우 발생. 아예 lost 리스트에서 제거함으로써 방지.
    # if cnt > n: # 7번 테케. 왜인지 모르겠지만 n보다 큰 값이 cnt되는 경우 존재 -> n으로 변경
    #     cnt = n
    # answer = cnt
    
    return answer