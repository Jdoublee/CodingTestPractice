def solution(strings, n):
    # s:s[n] - s[n]을 기준으로 정렬
    # 문제 추가 조건 - 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.
    # s 추가 후 괄호로 묶어줌
    return sorted(strings, key=lambda s:(s[n], s)) 