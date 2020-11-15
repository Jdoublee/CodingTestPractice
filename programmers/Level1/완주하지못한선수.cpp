// 정렬 후 비교 진행
// hash로 구현해보기
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    int i;
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    for(i=0;i<completion.size();i++){
        if(participant[i]==completion[i])
            continue;
        break;
    }
    answer=participant[i];
    
    return answer;
}