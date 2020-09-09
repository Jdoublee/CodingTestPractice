// dfs로 풀이
// 이건 예전에 푼 방법
// 다시 풀었는데 저장 안 해둠,,,
// **다시 풀어보기
#include <iostream>
#include <algorithm>
using namespace std;
int danji_num=0;
int tot[314]={0,};//최대 단지수 (n^2+1)/2
int graph[26][26]={-1,};
int dir[4][2]={{1,0},{0,1},{-1,0},{0,-1}};
void dfs(int y,int x,int n){
	graph[y][x]=-1;
	tot[danji_num]++;
	
	int dy,dx;
	int cur;
	for(int i=0;i<4;i++){
		dx=x+dir[i][0];
		dy=y+dir[i][1];
		cur=graph[dy][dx];
		if(0<=dy&&dy<n&&0<=dx&&dx<n&&cur==1)
			dfs(dy,dx,n);
	}
}
void search(int n){
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
			if(graph[i][j]==1){
				danji_num++;
				dfs(i,j,n);
			}
}
int main() {
	int n;
	cin>>n;
	
	for(int i=0;i<n;i++){
		string s;
		cin>>s;
		for(int j=0;j<n;j++){
			if(s[j]=='0')
				graph[i][j]=0;
			else
				graph[i][j]=1;
		}
	}
	search(n);
	
	sort(tot+1,tot+1+danji_num);
	cout<<danji_num<<"\n";
	if(danji_num>0){
		for(int i=1;i<=danji_num;i++)
			cout<<tot[i]<<"\n";
	}

	return 0;
}