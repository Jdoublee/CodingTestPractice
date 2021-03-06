#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main() {
    int n;
	int mx=0;
	cin>>n;
	vector<int> v(n);
	for(int i=0;i<n;i++){
		cin>>v[i];
	}
	sort(v.begin(),v.end());
	for(int i=0;i<n;i++){
		if(mx<v[i]*(n-i))
			mx=v[i]*(n-i);
	}
    // 큰 수부터 비교하고 빠져나가는 건 왜 안될까
    // for(int i=n-1;i>=0;i--){
    //         if(v[i]*(n-i)>=mx)
    //             mx=v[i]*(n-i);
    //         else
    //             break;
    //     }


	cout<<mx<<"\n";
    return 0;
}
