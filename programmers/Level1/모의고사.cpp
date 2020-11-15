// 완전탐색
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> cnt(3);
    vector<int> cmpv(3);
    int arr1[] = {1,2,3,4,5}; // 5
    int arr2[] = {2,1,2,3,2,4,2,5}; // 8
    int arr3[] = {3,3,1,1,2,2,4,4,5,5}; // 10
    // 모듈러 연산 사용하여 위 배열 순환 사용
    for(int i=0;i<answers.size();i++){
        if(answers[i]==arr1[i%5])  cnt[0]++;
        if(answers[i]==arr2[i%8])  cnt[1]++;
        if(answers[i]==arr3[i%10])  cnt[2]++;         
    }
    for(int i=0;i<cnt.size();i++)
        cmpv[i]=cnt[i];

    sort(cmpv.begin(), cmpv.end()); // 최댓값 찾기 위해서

    for(int i=0;i<cnt.size();i++)
        if(cmpv[2]==cnt[i]) // 최댓값과 비교하여 같으면 답에 추가
            answer.push_back(i+1);
    
    return answer;
}