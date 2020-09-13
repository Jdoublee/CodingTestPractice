// 시간 초과 에러 -> cin cout 속도 느려서
// 1) printf scanf 사용
// 2) ios_base :: sync_with_stdio(false);
// cin.tie(NULL);
// cout.tie(NULL);
// 작성해줌
// 이분탐색 보자고 해놓고 안보다 사단이 났다^^ 
// 이진탐색으로 부분합 개념 잡기

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios_base :: sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int n,m;
	vector<int> A;
	cin>>n;
	for(int i=0;i<n;i++){
		int x;
		cin>>x;
		A.push_back(x);
	}
	sort(A.begin(),A.end());
	
	cin>>m;
	for(int i=0;i<m;i++){
		int x;
		cin>>x;
        // lower_bound 함수는 주어진 수의 위치를 반환. 주어진 수가 존재하지 않는다면 주어진 수보다 큰 가장 작은 수의 위치를 반환
		int res=lower_bound(A.begin(),A.end(),x) - A.begin(); // iterator 이므로 시작 주소 빼줌
		if(A[res]==x)
			cout<<1<<"\n";
		else
			cout<<0<<"\n";
	}
	
	return 0;
}