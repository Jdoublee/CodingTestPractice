def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        res = ""
        cnt = 1
        first = s[:i]
        
        for j in range(i, len(s)+i, i):
            cmp = s[j:j+i]
            if len(first) != len(cmp):
                if cnt > 1:
                    res += str(cnt)
                res += first
                if cmp != "":
                    res += cmp
                break
                
            if first == cmp:
                cnt += 1
            else:
                if cnt > 1:
                    res += str(cnt)
                res += first
                cnt = 1
            first = cmp
            
        if answer > len(res) :
            answer = len(res)
            
    return answer

x = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]

for s in x:
    print(solution(s))