#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int t,n;
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>n;
		int cnt=0;
		vector<pair<int,int>> v(n);
		for(int j=0;j<n;j++)
			cin>>v[j].first>>v[j].second;
		sort(v.begin(),v.end()); // 서류 순위 기준으로 오름차순 정렬
		int pivot=v[0].second; // 면접 순위 기준으로 비교하면 됨. 서류 1등 순위가 기준.
		for(int j=0;j<n;j++){
			if(pivot>=v[j].second){ // 0부터 세기 때문에 1등 카운트해주려고 = 기호 붙여줌.
				cnt++;
				pivot=v[j].second; // 직전 채용된 사원을 새로운 기준으로 대입.
			}
		}
		cout<<cnt<<"\n";
		
	}
	return 0;
}

        // TLE - for문이 몇개여,,, 효율적인 코드를 짜자
        // for(int j=0;j<n;j++){
        //             bool res=true;
        //             for(int k=j-1;k>=0;k--){
        //                 if(v[j].second>v[k].second){
        //                     res=false;
        //                     break;
        //                 }
        //             }
        //             if(res==true)
        //                 cnt++;
        //         }
