#include <iostream>
#include <stack>
using namespace std;

int main() {
	string s;
	while(true){
		string res="yes"; // default : yes
		stack<char> st;
		getline(cin,s); // 한 줄 씩 입력받기 (공백 포함)
		if(s==".") // 종료 조건
			break;
		for(int i=0;i<s.size();i++){
			if(s[i]=='('||s[i]=='[')
				st.push(s[i]);
			else if(s[i]==')'){
				if(st.empty()){ // 스택 비었을 경우 추가
					res="no";
					break;
				}
				if(st.top()=='(')
					st.pop();
				else{ // '[', ']', ')' 
					res="no";
					break;
				}
			}else if(s[i]==']'){
				if(st.empty()){ // 스택 비었을 경우 추가
					res="no";
					break;
				}
				if(st.top()=='[')
					st.pop();
				else{ //  '(', ')', ']'
					res="no";
					break;
				}
			}
		}
		if(!st.empty())
			res="no";
		cout<<res<<"\n";
	}
	
	return 0;
}