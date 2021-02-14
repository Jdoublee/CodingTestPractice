def solution(s):    
    st = []
    
    for x in s:
        if x == '(':
            st.append(x)
        elif not st:
            return False
        elif st.pop() == '(':
            continue
        else:
            return False
    if st:
        return False

    return True