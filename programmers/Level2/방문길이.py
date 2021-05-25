def solution(dirs):
    answer = 0
    
    dx = {'U':1, 'D':-1, 'L':0, 'R':0}
    dy = {'U':0, 'D':0, 'L':-1, 'R':1}
    
    visited = []
    
    x = 5
    y = 5
    
    for d in dirs:
        nx = x + dx[d]
        ny = y + dy[d]
        
        if 0 > nx or 10 < nx or 0 > ny or 10 < ny:
            continue
        
        points = [(x,y),(nx,ny)]
        points.sort()
        
        if points not in visited:
            visited.append(points)
            answer += 1
        
        x,y = nx,ny
        
    return answer