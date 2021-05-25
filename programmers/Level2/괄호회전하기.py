def solution(s):
    answer = 0
    
    f = ['[','(','{']
    b = [']',')','}']
    
    s = list(s)
    st = []
    
    for i in range(len(s)):
        flag = True
        for x in s:
            if x in f:
                st.append(x)
            elif st:
                top = st.pop()
                if top not in f or x not in b or f.index(top) != b.index(x):
                    flag = False
                    break
            else:
                flag = False
                break
                
        if flag and not st:
            answer += 1
        
        tmp = s[0]    
        s = s[1:]
        s.append(tmp)
    
    return answer