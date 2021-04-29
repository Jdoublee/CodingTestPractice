from collections import deque

def bfs(maps,n,m):
    dx = [-1,0,0,1]
    dy = [0,-1,1,0]
    
    q = deque()
    q.append((0,0))
    
    while q:
        x,y = q.popleft()
        
        if x == n-1 and y == m-1:
            return maps[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                q.append((nx,ny))
                maps[nx][ny] = maps[x][y] + 1
                
    return -1

    
def solution(maps):
    
    return bfs(maps,len(maps),len(maps[0]))