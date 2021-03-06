// dfs 와 bfs 기본 알고리즘 구조 파악하기 좋은 문제
// 차이 및 사용법 익히자
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
void dfs(int s,vector<int> graph[],bool visited[]){
	visited[s]=true;
	cout<<s<<" ";
	
	for(int i=0;i<graph[s].size();i++){
		int next=graph[s][i];
		
		if(!visited[next])
			dfs(next,graph,visited);
	}
}
void bfs(int s,vector<int> graph[],bool visited[]){
	queue<int> q;
	
	q.push(s);
	visited[s]=true;
	
	while(!q.empty()){
		int start=q.front();
		q.pop();
		cout<<start<<" ";
		
		for(int i=0;i<graph[start].size();i++){
			int next=graph[start][i];
			
			if(!visited[next]){
				q.push(next);
				visited[next]=true;
			}
		}
	}
}
int main() {
	int n,m,v;
	cin>>n>>m>>v;
	
	vector<int> graph[n+1];
	bool visited[n+1];
	fill(visited,visited+(n+1),false);//bool false로 값 초기화
	
	for(int i=0;i<m;i++){
		int u,v;
		cin>>u>>v;
		
		graph[u].push_back(v);
		graph[v].push_back(u);
	}
	
	for(int i=0;i<n;i++)
		sort(graph[i+1].begin(),graph[i+1].end());
	
	dfs(v,graph,visited);
	cout<<"\n";
	fill(visited,visited+(n+1),false);
	bfs(v,graph,visited);
	cout<<"\n";
	
	return 0;
}