#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
bool cmp(const pair<int,int>&a, const pair<int,int>&b){
	if(a.second==b.second) // y좌표가 같으면 x좌표가 증가하는 순서로 정렬
		return a.first<b.first;
	return a.second<b.second; // y좌표가 증가하는 순
}
int main() {
	int n;
	cin>>n;
	vector<pair<int,int>> v(n);
	for(int i=0;i<n;i++)
		cin>>v[i].first>>v[i].second;
	sort(v.begin(),v.end(),cmp);
	for(int i=0;i<n;i++)
		cout<<v[i].first<<" "<<v[i].second<<"\n";
	return 0;
}