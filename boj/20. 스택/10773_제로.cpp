// stl 사용하면 편-안
// 오랜만에 문제 푸니 헷갈리는데 stl 자유자재로 사용할 수 있게
// 꾸준히 풀자.
#include <iostream>
#include <stack>
using namespace std;

int main() {
	int k;
	int tot=0;
	stack<int> st;
	cin>>k;
	
	for(int i=0;i<k;i++){
		int tmp;
		cin>>tmp;
		if(tmp==0)
			st.pop();
		else
			st.push(tmp);
	}
	while(!st.empty()){
		tot+=st.top();
		st.pop();
	}
	cout<<tot<<"\n";
	
	return 0;
}