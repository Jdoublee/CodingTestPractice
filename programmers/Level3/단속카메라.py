import copy

def solution(routes):
    answer = 0
    
    # 사람들이 올려놓은 TC 중에 [10, 5]와 같이 진입점이 진출점보다 큰 경우 존재해서 넣어줬는데
    # 해당 문제 채점 TC에는 해당 경우 고려 안 함
    # routes = [[a,b] if a<b else [b,a] for a,b in routes]
            
    routes.sort(key=lambda x:x[1]) # 진출 시간 기준으로 정렬.
    
    while routes:
        # 진출 시간이 가장 이른 경우 pop
        now = routes.pop(0)
        answer += 1
        
        # 해당 시점에 카메라 달았을 떄, 찍히는 경우 체크하기 위해 남은 루트 tmp 리스트에 넣어줌
        tmp = copy.deepcopy(routes)
        
        while tmp:
            a, b = tmp.pop(0)
            # 해당 카메라 단 시점(진출 시간이 가장 빠른 차량의 진출 시점)에 고속도로 이용중인 차량은 제거해줌(찍혔으니까~)
            if a <= now[0] <= b or a <= now[1] <= b:
                routes.pop(0)
            else:
                break

    return answer