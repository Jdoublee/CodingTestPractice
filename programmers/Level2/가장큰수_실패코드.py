# 테케 및 반례는 다 통과하는데 1~6 통과 못 함... 왜인지 모름 -> 다른 비교 방식 사용(더 간결함)
def solution(numbers):
    answer = ''
    num = list(map(str, numbers))
    num.sort(reverse=True)
    i = '1'
    li = []
    for n in num:
        if n[0] == i:
            li.append(n)            
        else:
            if len(li) > 1 :
                leng = len(li[0])
                n_li = []
                for l in li :
                    a = l + i * (leng + 1 - len(l))
                    n_li.append((a,l)) # a는 비교 위해 뒤에 값 붙여준 애들, l은 원래 원소
                    # [3, 30, 34, 5, 9] , "9534330" 에서 [3, 30, 34] 비교 -> [333, 303, 343] 다시 정렬후 원래 원소 answer에 추가
                n_li.sort(reverse=True)
                for l in n_li :
                    answer += l[1]
            elif len(li) == 1 :
                answer += li[0]
            i = n[0]
            li = [n]
    # 남은 애들 처리
    leng = len(li[0])
    n_li = []
    for l in li :
        a = l + i * (leng + 1 - len(l))
        n_li.append((a,l))
    n_li.sort(reverse=True)
    for l in n_li :
        answer += l[1]            
    answer = str(int(answer)) # [0,0,0] , "0" 의 경우를 위해 int형으로 한 번 변환한 후 다시 str로 저장
    return answer