// 5분, 1분, 10초
#include <iostream>
#include <vector>
using namespace std;

int main() {
	int t;
	vector<int> v(3,0);
	cin>>t;
	
	if(t%10>0){
		cout<<-1<<"\n";
		return 0;
	}
	while(t>0){
		if(t>=300){
			v[0]+=1;
			t-=300;
		}else if(t>=60){
			v[1]+=1;
			t-=60;
		}else{
			v[2]+=1;
			t-=10;
		}
	}
	for(int i=0;i<v.size();i++)
		cout<<v[i]<<" ";
	return 0;
}