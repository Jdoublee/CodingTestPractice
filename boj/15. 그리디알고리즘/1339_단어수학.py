n = int(input())
nums = [] # 각 문자에 해당될 자연수 정하기 위한 연산 값(tuple 형태) 저장
origin = [] # 입력 문자들 저장
chrs = [[0] * 8 for _ in range(10)]
dic1 = {} # 대문자 알파벳 모두 가능 (A-Z). 개수 제한만 존재. 입력으로 키-값 채움.
dic3 = {}

for _ in range(n):
	n = input()
	idx = 7
	for c in n[::-1]:
		if c not in dic1.keys():
			dic1[c] = len(dic1.keys())
		chrs[dic1[c]][idx] += 1
		idx -= 1
	origin.append(n)

dic2 = {v:k for k,v in dic1.items()}
for i in range(10):
	start = 0
	num = 0
	for j in range(8):
		if chrs[i][j] == 0 and start == 0:
			continue
		start = 1
		num = num*10 + chrs[i][j]
	nums.append((num, i))

nums.sort(reverse=True)
val = 9
for a, b in nums:
	if a == 0:
		break
	dic3[dic2[b]] = val
	val -= 1
	
res = 0
for words in origin:
	val = 0
	for word in words:
		val *= 10
		val += dic3[word]
	res += val
print(res)