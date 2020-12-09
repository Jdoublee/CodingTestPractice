n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

sorted_a = sorted(a)
sorted_b = sorted(b, reverse=True)

for i in range(k) :
	if sorted_a[i] < sorted_b[i] :
		sorted_a[i], sorted_b[i] = sorted_b[i], sorted_a[i]
	else :
		break

print(sum(sorted_a))