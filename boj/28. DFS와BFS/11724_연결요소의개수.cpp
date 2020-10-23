#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
// vector는 &로 주소값 불러와야 값 수정 가넝
// 배열로 넘겨버리자
// DFS 기본 응용하기 - 모든 경로를 탐색하고 결과를 확인해야 하는 경우 였슴다
void dfs(vector<int> graph[], vector<bool> &visited, int s){ 
	visited[s]=true;
	
	for(int j=0;j<graph[s].size();j++){
		int next=graph[s][j];
		
		if(!visited[next])
			dfs(graph,visited,next);
	}
}
int main() {
	int n,m,i;
	int cnt=0;
	cin>>n>>m;
	vector<int> graph[n+1];
	vector<bool> visited(n+1,false);
	for(i=0;i<m;i++){
		int u,v;
		cin>>u>>v;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}
	for(i=1;i<n+1;i++)
		sort(graph[i].begin(),graph[i].end());
	i=1; // 요소 1번부터 시작 
	while(i<=n){
		if(!visited[i]){ // 방문 안 한 노드들로 시작 후 cnt++
			dfs(graph,visited,i);
			cnt++;
		}
		i++;
	}
	cout<<cnt<<"\n";
	
	return 0;
}