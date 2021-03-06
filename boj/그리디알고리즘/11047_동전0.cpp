#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n,k,i;
	int tot=0,cnt=0;
	cin>>n>>k;
	vector<int> v(n);
	int kk=k;
    
	for(i=0;i<n;i++){
		cin>>v[i];
	}
	i--;
	while(i>=0){
		if(v[i]<=kk){
			tot+=v[i];
			kk-=v[i];
			cnt++;
		}
		else{
			i--;
		}
		if(tot==k)
			break;
	}
	cout<<cnt<<"\n";
	
	return 0;
}