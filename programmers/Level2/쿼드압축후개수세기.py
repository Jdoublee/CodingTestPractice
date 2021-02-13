def solution(arr):
    res = []
        
    def check(x,y,m):
        n = (m // 2)

        narr = [ar[y:y+n] for ar in arr[x:x+n]] # 2차원 배열 slicing 이렇게 해줘야 함. [:][:] 연달아 사용 불가~_~
        if sum(map(sum, narr)) == n*n:
            res.append(1)
        elif sum(map(sum, narr)) == 0:
            res.append(0)
        else:
            check(x,y,n)
        
        narr = [ar[y+n:y+m] for ar in arr[x:x+n]]
        if sum(map(sum, narr)) == n*n:
            res.append(1)
        elif sum(map(sum, narr)) == 0:
            res.append(0)
        else:
            check(x,y+n,n)
        
        narr = [ar[y:y+n] for ar in arr[x+n:x+m]]
        if sum(map(sum, narr)) == n*n:
            res.append(1)
        elif sum(map(sum, narr)) == 0:
            res.append(0)
        else:
            check(x+n,y,n)
        
        narr = [ar[y+n:y+m] for ar in arr[x+n:x+m]]
        if sum(map(sum, narr)) == n*n:
            res.append(1)
        elif sum(map(sum, narr)) == 0:
            res.append(0)
        else:
            check(x+n,y+n,n)       
            
    # 처음에 주어진 arr 다 0 이거나 1인지 확인 후 check 재귀 확인
    if sum(map(sum, arr)) == len(arr)*len(arr):
        return [0, 1]
    elif sum(map(sum, arr)) == 0:
        return [1, 0]
    
    check(0,0,len(arr))
            
    
    return [res.count(0), res.count(1)]