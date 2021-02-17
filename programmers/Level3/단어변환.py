from collections import deque

def difone(a, b):
    cnt = 0
    
    for a1, b1 in zip(a, b):
        if a1!=b1:
            cnt += 1
    
    if cnt == 1:
        return True
    else:
        return False
            
        
def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = 0
            
    visited = [False] * len(words)
    
    q = deque()
    q.append(begin)
    
    while q:
        now = q.popleft()
        tmp = deque()
        answer += 1

        for i, word in enumerate(words):
            if difone(now,word) and not visited[i]:
                if word == target:
                    return answer

                visited[i] = True
                tmp.append(word)
        
        q = tmp
    
    return answer