#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    queue<pair<int,int>> q;
    
    for(int i=0;i<priorities.size();i++)
        q.push(make_pair(priorities[i],i)); // <중요도, 위치> 저장
    
    sort(priorities.begin(),priorities.end()); // 중요도 정렬 후, 가장 높은 중요도 기준으로 비교 진행
    
    int a,b;
    while(true){
        // 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
        a=q.front().first;
        b=q.front().second;
        // 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
        if(a<priorities.back()){
            q.pop();
            q.push(make_pair(a,b));
        }
        // 3. 그렇지 않으면 J를 인쇄합니다.
        else{
            answer++; // 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 저장
            if(b==location)
                break;
            q.pop();
            priorities.pop_back();
        }
    }
    
    return answer;
}