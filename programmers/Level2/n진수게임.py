# divmod 라는 꿀 내장함수가 있다
# n진수 만들기 등 잘 활용하자
def nnum(k, n):
	c = '0123456789ABCDEF'
	q, r = divmod(k, n)
    
	if q == 0:
		return c[r]
    
	return nnum(q, n) + c[r]
    

def solution(n, t, m, p):
    answer = ''
        
    length = m * (t-1) + p
    
    now = 0
    
    game = ''
    
    while length >= len(game):
        game += nnum(now, n)
        now += 1
        
    answer = game[p-1::m]
    
    if len(answer) > t:
        tmp = game[p-1::m]
        answer = tmp[:t]
    
    return answer

# 아래는 divmod 안 쓰고 직접 구현했는데 1~7, 25번 테케빼고 실패뜸
# 끄응 divmod 짱
# 뭐가 문제였을까
#
# def nnum(n, k):
#     if k == 0:
#         return ['0']
#     if k == 1:
#         return ['1']
#     if k >= n:
# 	    flag = True
#     else:
#         flag = False
#     li = []
#     dic = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
#     while k > 1:
#         rem = k % n
#         if n > 10 and rem >= 10:
#             rem = dic[rem]
#         li.append(str(rem))
#         k //= n
#     if flag:
#         li.append('1')
#     li.reverse()
#     return li
    

# def solution(n, t, m, p):
#     answer = ''
    
#     # print(nnum(2, 1))
    
#     length = m * (t-1) + p
#     # print(length)
#     nowlen = 0
#     now = 0
    
#     game = ''
    
#     while length >= nowlen:
#         tmp = nnum(n, now)
#         now += 1
#         temp = ''.join(tmp)
#         game += temp
#         nowlen += len(temp)
    
#     # print(game)
#     # print(game[p-1::m])
    
#     if len(game[p-1::m]) > t:
#         tmp = game[p-1::m]
#         return tmp[:t]
#     else:
#         return game[p-1::m]
    
#     return answer