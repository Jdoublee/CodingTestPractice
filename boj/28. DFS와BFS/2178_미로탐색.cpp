// bfs로 풀이
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int graph[100][100];
int n,m;
void bfs(int x, int y){
	int dx[]={0,0,1,-1};
	int dy[]={-1,1,0,0};
	queue<pair<int,int>> q;
	q.push(make_pair(0,0));
	pair<int,int> cur;
	
	while(!q.empty()){
		cur=q.front();
		q.pop();
		
		for(int i=0;i<4;i++){
			int nx=cur.second+dx[i];
			int ny=cur.first+dy[i];
			if(nx>=0&&ny>=0&&nx<m&&ny<n&&graph[ny][nx]==1){
				q.push(make_pair(ny,nx));
				graph[ny][nx]=graph[cur.first][cur.second]+1;
			}
		}
	}
}
int main() {
	string s;
	cin>>n>>m;
	
	for(int i=0;i<n;i++){
		cin>>s;
		for(int j=0;j<m;j++){
			if(s[j]=='0')
				graph[i][j]=0;
			else
				graph[i][j]=1;
		}
	}
	bfs(0,0);
	cout<<graph[n-1][m-1]<<"\n";
	return 0;
}