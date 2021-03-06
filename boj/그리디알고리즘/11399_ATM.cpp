#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n;
	int tot=0;
	int bef=0;
	cin>>n;
	vector<int> v(n);
	
	for(int i=0;i<n;i++)
		cin>>v[i];

	sort(v.begin(),v.end());
    
	for(int i=0;i<n;i++){
		bef += v[i];
		tot += bef;
	}
	cout<<tot<<"\n";
	return 0;
}