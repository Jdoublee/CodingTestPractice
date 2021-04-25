import sys
sys.setrecursionlimit(10**6)

def solution(k, room_number):
    answer = []
    parent = {}
    
    def find(x):
        if x not in parent:
            parent[x] = x
        elif parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]


    def union(a):
        parent[a] = find(a+1)


    for rn in room_number:
        room = find(rn)
        answer.append(room)
        
        union(room)
    
    return answer
# 백준 공항 문제와 유사