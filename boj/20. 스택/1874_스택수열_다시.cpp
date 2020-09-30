// 한 번 더 보기
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int main() {
	int n,idx=0;
	stack<int> st; // 1~n 정수 스택
	vector<char> v; // 출력(+, -) 위한 벡터
	vector<int> s; // 입력 저장 벡터
	cin>>n;

	for(int i=0;i<n;i++){
		int tmp;
		cin>>tmp;
		s.push_back(tmp);
	}
	for(int i=1;i<=n;i++){
		st.push(i);
		v.push_back('+');
		
		while(!st.empty()&&st.top()==s[idx]){
			st.pop();
			v.push_back('-');
			idx++;
		}
	}
	if(!st.empty())
		cout<<"NO"<<"\n";
	else
		for(int i=0;i<v.size();i++)
			cout<<v[i]<<"\n";
	
	return 0;
}