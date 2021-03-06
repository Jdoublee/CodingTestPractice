#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
bool cmp(const pair<int,int> &a, const pair<int,int> &b){
	if(a.first==b.first)
		return a.second<b.second;
	return a.first<b.first;
}
int main() {
	int n;
	cin>>n;
	vector<pair<int,string>> v(n);
	vector<pair<int,int>> vi;
	
	for(int i=0;i<n;i++){
		cin>>v[i].first>>v[i].second;
		vi.push_back(make_pair(v[i].first,i)); // 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로
	}
	sort(vi.begin(),vi.end(),cmp);
	for(int i=0;i<n;i++){
		cout<<vi[i].first<<" "<<v[vi[i].second].second<<"\n";
	}
	
	return 0;
}