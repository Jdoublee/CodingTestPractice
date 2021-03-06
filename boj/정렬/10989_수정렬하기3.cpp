// 시간초과, 메모리 초과 골고루 났던 문제
// 카운팅소트 개념 -> 약간의 변형
#include <iostream>
using namespace std;
int cnt[10001]={0};
int main() {
    // 시간초과 방지
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
	int n;
	int max=0;
	cin>>n;
	for(int i=0;i<n;i++){
		int tmp;
		cin>>tmp;
		cnt[tmp]++;
		if(max<tmp)
			max=tmp;
	}
	for(int i=0;i<=max;i++)
        for(int j=0;j<cnt[i];j++)
        	cout<<i<<"\n";
	return 0;
}