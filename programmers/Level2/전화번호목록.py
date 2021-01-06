def solution(phone_book):
    # answer = True
    
    phone_book.sort(key=lambda p:len(p)) # key 사용하여 문자열 길이 순으로 정렬

    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False
        #         answer = False
        #         break
        # if not answer:
        #     break
    
    return True
    # return answer

    # 이렇게 풀어도 시간 초과 안나고 효율성도 다 통과함
    # 해쉬 사용해서 다시 풀어보기