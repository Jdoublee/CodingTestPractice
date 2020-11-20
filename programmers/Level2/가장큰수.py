def solution(numbers):
    num = list(map(str, numbers))
    num.sort(key=lambda x : x*3 , reverse=True) # lambda 이용 간단하게 코드 짤 수 있음
    answer = str(int(''.join(num))) # [0,0,0] , "0" 의 경우를 위해 int형으로 한 번 변환한 후 다시 str로 저장
    return answer