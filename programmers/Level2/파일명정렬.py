def solution(files):
    answer = []
    
    res = []
    
    eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .-' # 개빡친다^^ 오타 죽여버려^^ 정규표현식 쓰기 싫어서(찾아보기 귀찮아서) 이렇게 선언했는데 j를 z라고 쓴 멍청이^^ 런타임에러 혹시나 했다^^ 
    num = '1234567890'
    for file in files:
        head = ''
        number = ''
        tail = ''
        now = 0
        limit = 0
        
        for i, f in enumerate(file):
            if now == 0:
                if f in eng:
                    head += f
                else:
                    number += f
                    now += 1
                    limit += 1
            elif now == 1 and limit < 5: # 숫자 부분 최대 5자리까지!
                if f in num:
                    number += f
                    limit += 1
                else:
                    tail += f
                    now += 1   
            else:
                tail += file[i:] # 꼬리 부분 한 번에 처리
                break
        res.append([head, number, tail])
    
    res.sort(key=lambda r:(r[0].lower(), int(r[1]))) # 대소문자 구별x, 숫자끼리 비교
    
    for r in res:
        answer.append(''.join(r))
        
    return answer