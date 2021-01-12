import heapq
def solution(operations):
    
    h = []
    
    for op in operations:
        o, n = op.split()
        
        if o == 'I':
            heapq.heappush(h, int(n))
        elif h == []:
            continue
        elif n == '1':
            h.pop()
        else:
            h.pop(0)
                
    if h == []: # if not h: 와 동일
        return [0, 0]
    
    return [h.pop(),h.pop(0)]

# 이렇게 해도 풀리는데 최대힙 최소힙 따로 두 개 구현해서 웅앵합시다