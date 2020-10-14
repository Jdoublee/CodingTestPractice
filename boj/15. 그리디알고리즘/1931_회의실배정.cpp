#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// vector의 pair쌍 중 두번째 값 기준으로 정렬하기 위해 선언
bool compare(const pair<int,int>&a, const pair<int,int>&b){
	if(a.second==b.second) // 끝나는 시간 같은 경우, 시작하는 시간이 이른 것이 먼저 오도록 조건 추가
		return a.first<b.first;
	else
		return a.second<b.second;
}
int main() {
	int n;
	cin>>n;
	vector<pair<int,int>> v(n);
	int now,cnt=0;
	for(int i=0;i<n;i++){
		cin>>v[i].first>>v[i].second;
	}
	sort(v.begin(),v.end(),compare); // 회의 시간 정렬
	now=0; // 끝나는 시간 기준
	cnt++;
	for(int i=1;i<n;i++){
		if(v[now].second<=v[i].first){
			now=i;
			cnt++;
		}
	}
	cout<<cnt<<"\n";
	
	return 0;
}