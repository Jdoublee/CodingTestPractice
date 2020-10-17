// 500엔, 100엔, 50엔, 10엔, 5엔, 1엔
#include <iostream>
using namespace std;

int main() {
	int n, m;
	int cnt=0;
	cin>>n;
	
	m = 1000-n;
	while(m>0){
		if(m>=500){
			m-=500;
			cnt++;
		}else if(m>=100){
			m-=100;
			cnt++;
		}else if(m>=50){
			m-=50;
			cnt++;
		}else if(m>=10){
			m-=10;
			cnt++;
		}else if(m>=5){
			m-=5;
			cnt++;
		}else{
			m-=1;
			cnt++;
		}
	}
	cout<<cnt<<"\n";
	return 0;
}