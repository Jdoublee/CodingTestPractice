// BFS 문제 - 최단 경로
// 빡대갈쓰ㅠ
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
	int n,a,b,m;
	int u,v;
	cin>>n;
	vector<int> graph[n+1];
	vector<int> cnt(n+1,0); // 각 그래프 방문여부 + 촌수 cnt. 0으로 초기화.
	cin>>a>>b;
	cin>>m;
	for(int i=0;i<m;i++){
		cin>>u>>v;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}
	// bfs
	queue<int> q;
	q.push(a);
	while(!q.empty()){
		int now=q.front();
		q.pop();

		for(int i=0;i<graph[now].size();i++){
			int next=graph[now][i];
			if(cnt[next]!=0) // 방문한적 있으면 continue
				continue;
			q.push(next);
			cnt[next]=cnt[now]+1; // 첨이면 cnt++해서 next에 추가
		}
	}
	
	cout<<(cnt[b]>0 ? cnt[b]:-1)<<"\n"; // 삼항연산 출력할 때 괄호 꼭,,, > 등의 문자를 인식 못해부린다. 
	
	return 0;
}