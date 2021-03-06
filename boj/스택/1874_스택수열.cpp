// STL stack 써서 다시 풀어보기
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
vector<int> stack;
queue<int> output;
int main() {
	int n,x,max;
	cin>>n;
	//int arr[n]={0};
	max=0;
	for(int i=0;i<n;i++){
		cin>>x;
		if(max<x){
			for(int j=max+1;j<=x;j++){
				//arr[j]=1;
				stack.push_back(j);
				output.push(1);
				//cout<<"+\n";
			}
			max=x;
			stack.pop_back();
			output.push(0);
			//cout<<"-\n";
		}
		else{
			if(x!=stack.back()){
				//cout<<"NO\n";
				output.push(2);
				break;
			}
			stack.pop_back();
			output.push(0);
			//cout<<"-\n";
		}
	}
	while(output.size()>0){
		if(output.back()==2){
			cout<<"NO"<<"\n";
			break;
		}
		if(output.front()==0){
			cout<<"-"<<"\n";
			output.pop();
		}else{
			cout<<"+"<<"\n";
			output.pop();
		}
		
		
	}

	return 0;
}