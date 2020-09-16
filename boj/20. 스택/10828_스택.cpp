// 일 년 전에 짠 코드
// 더 깔끔하게 다시 짜보기
#include <iostream>
using namespace std;

int stack[10000];
int idx=-1;

void push(int x){
	stack[++idx]=x;
}
void pop(){
	if(idx==-1)
		cout<<-1<<"\n";
	else
		cout<<stack[idx--]<<"\n";
}
void size(){
	cout<<idx+1<<"\n";
}
void empty(){
	if(idx==-1)
		cout<<1<<"\n";
	else
		cout<<0<<"\n";
}
void top(){
	if(idx==-1)
		cout<<-1<<"\n";
	else
		cout<<stack[idx]<<"\n";
}
int main() {
	int n,m;
	string c;
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>c;
		if(c=="push"){
			cin>>m;
			push(m);
		}else if(c=="pop"){
			pop();
		}else if(c=="size"){
			size();
		}else if(c=="empty"){
			empty();
		}else if(c=="top"){
			top();
		}
	}
	
	return 0;
}
