#include <string>
#include <vector>
using namespace std;
vector<int> solution(vector<int> prices) {
    vector<int> answer;
    int n = prices.size();
    for(int i=0;i<n;i++){
        int res = 0;
        for(int j=i+1;j<n;j++){
            res++;
            if(prices[i]>prices[j])
                break;
        }
        answer.push_back(res);
    }
    return answer;
}