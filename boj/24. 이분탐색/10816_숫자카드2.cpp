// algorithm의 lower_bound 와 upper_bound 함수 사용
// 해당 원소의 시작 위치와 끝 위치(+1) 알려줌
// 이분탐색
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n,m,tmp;
	vector<int> v;
	vector<int> w;
	vector<int> res;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>tmp;
		v.push_back(tmp);
	}
	sort(v.begin(),v.end());
	cin>>m;
	for(int i=0;i<m;i++){
		cin>>tmp;
		int f=lower_bound(v.begin(),v.end(),tmp) - v.begin(); // 시작 위치
		if(v[f]!=tmp)
			res.push_back(0);
		else{
			int l=upper_bound(v.begin(),v.end(),tmp) - v.begin(); // 끝 위치 + 1 (다음 index)
			res.push_back(l-f); // [f.l) 개수 구하기위해 끝 구간끼리 빼줌.
		}
	}
	for(int i=0;i<m;i++){
		if(i<m-1)
			cout<<res[i]<<" ";
		else
			cout<<res[i]<<"\n";
	}
	
	
	
	return 0;
}