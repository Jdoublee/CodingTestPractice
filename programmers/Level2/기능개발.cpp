// 문제 조건 잘 읽기
#include <vector>
using namespace std;

int check(vector<int> v, int s){
    int i;
    for(i=s;i<v.size();i++){
        if(v[i]<100)
            break;
    }
    return i;
}
vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int idx=0;
    
    while(idx<progresses.size()){
        for(int i=idx;i<progresses.size();i++){
            progresses[i]+=speeds[i];
        }
        int ck=check(progresses, idx);
        if(ck>idx){
            answer.push_back(ck-idx);
            idx=ck;
        }
    }
    
    return answer;
}