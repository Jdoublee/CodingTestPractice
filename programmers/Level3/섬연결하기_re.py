# 크루스칼 알고리즘으로 다시 푼 섬 연결하기
def solution(n, costs):
    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]
    
    def union_parent(a, b):
        ap = find_parent(a)
        bp = find_parent(b)
        
        if ap < bp:
            parent[bp] = ap
        else:
            parent[ap] = bp
    

    parent = [i for i in range(n)] # 자기 자신으로 초기화
    res = 0 # 최소 비용 저장
    
    costs.sort(key=lambda x:x[2]) # 비용 기준으로 정렬
    
    for a,b,c in costs:
        if find_parent(a) != find_parent(b):
            union_parent(a,b)
            res += c
    
    return res