// 분해합/부분합 개념 다시 공부하기
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	int n, m, k, tot;
	cin>>n;
	vector<int> v;
	int res = n+1;
	for(int i=1;i<n;i++){
		k = m = i;
		tot = 0;
		while(true){
			tot += k;
			k = (m%10);
			if(k==0)
				break;
			m /= 10;
		}
		v.push_back(tot);
	}
	for(int i=0;i<v.size();i++){
		if(v[i]==n){
			res = i+1 < res ? i+1 : res;
		}
	}
	if(res==n+1)
		cout<<0<<"\n";
	else
		cout<<res<<"\n";
	return 0;
}