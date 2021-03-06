// 다시 문제, 코드 보기
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	vector<char> stack;
	int n;
	cin>>n;
	
	for(int i=0;i<n;i++){
		string vps,ans="\0";
		cin>>vps;
		int o=0,c=0,f=0;
		for(int j=0;j<vps.length();j++)
			stack.push_back(vps[j]);
		while(!stack.empty()){
			if(stack.back()=='('){
				o++;
				stack.pop_back();
			}else if(stack.back()==')'){
				c++;
				stack.pop_back();
			}
			if(o>c){
				ans="NO";
				f=1;
				while(!stack.empty())
					stack.pop_back();
				break;
			}
		}
		if(f!=1){
			if(o==c)
				ans="YES";
			else
				ans="NO";
		}
		cout<<ans<<"\n";
	}
	return 0;
}