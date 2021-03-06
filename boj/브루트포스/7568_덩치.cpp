// 문제를 잘 읽자
#include <iostream>
#include <vector>
using namespace std;

int main() {
	pair<int,int> p;
	vector<pair<int, int>> v;
	int n;
	cin>>n;
	vector<int> res(n, 0);
	
	for(int i=0;i<n;i++){
		int a,b;
		cin>>a>>b;
		p = make_pair(a,b);
		v.push_back(p);
	}
	
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if(i==j)
				continue;
			if(v[i].first<v[j].first&&v[i].second<v[j].second)
				res[i]+=1;	
		}
	}
	
	for(int i=0;i<n;i++)
		cout<<res[i]+1<<" ";
	cout<<"\n";
	return 0;
}