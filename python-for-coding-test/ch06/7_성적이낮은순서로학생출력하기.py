n = int(input())

student = []
for _ in range(n) :
    student.append(input().split())

result = sorted(student, key=lambda s : int(s[1])) # key 로 lambda 이용

for res in result :
	print(res[0], end=' ')