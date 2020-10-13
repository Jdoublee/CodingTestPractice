// t를 0부터 시작하는걸로 고치고싶다.
#include <string>
#include <vector>
#include <queue>
using namespace std;
int sum(queue<pair<int,int>> q){
    int tot=0;
    while(!q.empty()){
        tot+=q.front().first;
        q.pop();
    }
    return tot;
}
int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int t=1,i=0;
    queue<pair<int,int>> q;
    q.push(make_pair(truck_weights[i++],t));
    while(!q.empty()){
        t++;
        if(t-q.front().second==bridge_length)
            q.pop();
        if(i<truck_weights.size()&&sum(q)+truck_weights[i]<=weight){
            q.push(make_pair(truck_weights[i++],t));
        }
    }
    return t;
}