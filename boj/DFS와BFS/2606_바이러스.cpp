// dfs로 풀이
// cnt로 개수 파악
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
vector<int> graph[101]; //1부터 저장
bool visited[101];
int cnt=0;
void dfs(int s){
	visited[s]=true;

	for(int i=0;i<graph[s].size();i++){
		int next=graph[s][i];
		if(!visited[next]){
			cnt++;
			dfs(next);
		}
	}
}
int main() {
	int n,m;
	cin>>n>>m;
	
	for(int i=0;i<m;i++){
		int u,v;
		cin>>u>>v;
		
		graph[u].push_back(v);
		graph[v].push_back(u);
	}
	
	for(int i=0;i<n;i++)
		sort(graph[i+1].begin(), graph[i+1].end());
	dfs(1);
	cout<<cnt<<"\n";
	return 0;
}