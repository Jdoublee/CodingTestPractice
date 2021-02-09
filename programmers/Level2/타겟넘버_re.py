from collections import deque

def solution(numbers, target):    
    tree = deque([0])
    
    for num in numbers:
        tmp = deque()
        
        while tree:
            now = tree.popleft()
            
            tmp.append(now + num)
            tmp.append(now - num)
            
        tree.extend(tmp)
    
    return tree.count(target)