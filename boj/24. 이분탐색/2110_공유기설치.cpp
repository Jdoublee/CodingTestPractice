// 솔루션 해석이 어렵다 
// 밤이라 그런가 다시 보자 꼭 꼭
// 이분탐색은 어려워
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n,c;
	vector<int> v;
	cin>>n>>c;
	
	for(int i=0;i<n;i++){
		int tmp;
		cin>>tmp;
		v.push_back(tmp);
	}
	sort(v.begin(),v.end());
	
	int left=1; // 또는 0 . v[0]이 될 수 없음(반례 존재)
	int right=v[n-1];// 또는 v[n-1] - v[0]
	int res=-1;
	
	while(left<=right){
		int mid=(left+right)/2;
		int before=0;
		int cnt=1;
		
		for(int i=1;i<n;i++){
			if(v[i]-v[before]>=mid){
				before=i;
				cnt++;
			}
		}
		if(cnt>=c)
			left=mid+1;
		else
			right=mid-1;
			
		if(res<mid&&cnt>=c)
			res=mid;
	}
	cout<<res<<"\n";
	
	return 0;
}