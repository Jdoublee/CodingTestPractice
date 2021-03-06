#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n;
	cin>>n;
	vector<pair<int,int>> v(n);
	for(int i=0;i<n;i++)
		cin>>v[i].first>>v[i].second;
	sort(v.begin(),v.end());
	for(int i=0;i<n;i++)
		cout<<v[i].first<<" "<<v[i].second<<"\n";
	return 0;
}