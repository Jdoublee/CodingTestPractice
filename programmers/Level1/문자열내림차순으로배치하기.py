def solution(s):
    li = [w for w in s]
    li.sort(reverse=True)
    return ''.join(li)