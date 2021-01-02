def solution(n, arr1, arr2):
    answer = []
        
    for i in range(n):
        aa = bin(arr1[i])[2:] # 이진수로 변환. 0b 접두사 붙어있는 형태
        bb = bin(arr2[i])[2:]
        
        if len(aa) < n:
            aa = '0' * (n - len(aa)) + aa
        if len(bb) < n:
            bb = '0' * (n - len(bb)) + bb
        
        tmp = ''
        
        for j in range(n):
            if aa[j] == '1' or bb[j] == '1':
                tmp += '#'
            else:
                tmp += ' '
        
        answer.append(tmp)
    
    return answer