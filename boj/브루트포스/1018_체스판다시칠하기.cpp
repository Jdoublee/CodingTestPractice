// 아무리 완전탐색 문제라지만 넘 지저분하다.....
// 깔끔하게 짜고싶다 따흑
// 일단 구현이 먼저다
#include <iostream>
#include <vector>
using namespace std;
int checkBoard(vector<int> a, int t[]){
	int res=0;
	for(int i=0;i<8;i++){
		if(a[i]==t[i])
			continue;
		res++;
	}
	return res;
}
int main() {
	int n,m,min=2500;
	int cnt=0,cnt1=0,cnt2=0;
	char color;
	cin>>n>>m;
	vector<vector<int>> arr(n,vector<int>(m));
	vector<int> v;
	
	int testB[8]={0,1,0,1,0,1,0,1};
	int testW[8]={1,0,1,0,1,0,1,0};
	
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cin>>color;
			if(color=='B')
				arr[i][j]=0;
			else // 'W'
				arr[i][j]=1;
		}
	}
	for(int i=0;i<n;i++){
		if(i+8>n)
			break;
		for(int j=0;j<m;j++){
			if(j+8>m)
				break;
			for(int k=0;k<8;k++){
				for(int l=0;l<8;l++){
					v.push_back(arr[i+k][j+l]);
				}
				if(k%2==0){
					cnt1+=checkBoard(v, arr[i][j]==0?testB:testW);
					cnt2+=checkBoard(v, arr[i][j]==0?testW:testB);
				}
				else{
					cnt1+=checkBoard(v, arr[i][j]==0?testW:testB);
					cnt2+=checkBoard(v, arr[i][j]==0?testB:testW);
				}
				v.clear();
			}
			cnt=cnt1<cnt2?cnt1:cnt2;
			if(cnt<min)
				min=cnt;
			cnt=cnt1=cnt2=0;
		}
	}
	cout<<min<<"\n";
	
	return 0;
}