#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n, m, tot;
	int res=0;
	cin>>n>>m;
	vector<int> v;
	vector<int> sumv;

	for(int i=0;i<n;i++){
		int tmp;
		cin>>tmp;
		v.push_back(tmp);
	}
	
	sort(v.begin(), v.end());
	
	for(int i=0;i<n;i++){
		for(int j=i+1;j<n;j++){
			for(int k=j+1;k<n;k++){
				tot = v[i]+v[j]+v[k];
				sumv.push_back(tot);
			}
		}
	}

	for(int i=0;i<sumv.size();i++)
		if(sumv[i]<=m && sumv[i]>res)
			res=sumv[i];
            
	cout<<res<<" ";
	
	return 0;
}