// 피보나치 수 재귀로 풀기
// 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597 ...
#include <iostream>
using namespace std;
int fib(int n){
	if(n==0)
		return 0;
	if(n==1)
		return 1;
	return fib(n-2)+fib(n-1);
	
}
int main() {
	int n;
	cin>>n;
	
	cout<<fib(n)<<"\n";
	
	return 0;
}