// dfs로 풀이
// 네 방향 좌표 활용
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int tot=0;
int graph[50][50]={-1};
vector<int> v;
int dx[]={0,0,1,-1};
int dy[]={-1,1,0,0};

void dfs(int x, int y){
	graph[x][y]=-1;
	for(int i=0;i<4;i++){
		int nx=x+dx[i];
		int ny=y+dy[i];
		if(nx>=0&&ny>=0&&nx<50&&ny<50){
			if(graph[nx][ny]==1)
				dfs(nx,ny);
		}
	}
}
int main() {
	int t,m,n,k;
	cin>>t;
	for(int j=0;j<t;j++){
		cin>>m>>n>>k;
		for(int i=0;i<k;i++){
			int u,v;
			cin>>u>>v;
			graph[u][v]=1;
		}
		for(int l=0;l<m;l++)
			for(int c=0;c<n;c++)
				if(graph[l][c]==1){
					dfs(l,c);
					tot++;
				}
		cout<<tot<<"\n";
		tot=0;
		v.clear();
	}
	
	return 0;
}