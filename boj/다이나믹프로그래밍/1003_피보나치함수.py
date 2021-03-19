# 0과 1이 출력되는 횟수도 피보나치 함수
# 초기값(i=0,1) 설정 후 범위(0<=N<=40) 맞게 배열 채워줌
zeros = [1, 0]
ones = [0, 1]
 
for i in range(2, 41):
	zeros.append(zeros[i-2] + zeros[i-1])
	ones.append(ones[i-2] + ones[i-1])
 
t = int(input())
 
for _ in range(t):
	n = int(input())
	print(zeros[n], ones[n])