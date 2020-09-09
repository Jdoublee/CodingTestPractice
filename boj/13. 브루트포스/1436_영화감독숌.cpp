// 규칙 먼저 찾기
// 써보면서 찾는게 지금은 젤루 좋은 방법
// 말고 더 나은 방법이 있을까나
#include <iostream>
using namespace std;

int main() {
	int n, num=666, t;
	int cnt=0;
	cin>>n;

	while(cnt<10000){
		t = num;
		while(t!=0){
			if(t%1000==666){
				cnt++;
				break;
			}
			t /= 10;
		}
		if(cnt==n)
			break;
		num++;
	}
	cout<<num<<"\n";
	
	return 0;
}