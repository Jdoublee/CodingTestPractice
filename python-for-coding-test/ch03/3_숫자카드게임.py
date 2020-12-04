n, m = map(int, input().split())
cards = []

for i in range(n) :
	li = list(map(int, input().split()))
	li.sort()
	cards.append(li[0]) # 정렬 후 각 행의 가장 작은 값만 리스트에 저장 
cards.sort() # 저장해둔 작은 값들 다시 정렬 후 가장 큰 값 반환

print(cards[-1])


# min, max 사용 (책)
res = 0
for i in range(n) :
	li = list(map(int, input().split()))
	min_card = min(li)
	res = max(res, min_card)

print(res)