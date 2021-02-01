#include <bits/stdc++.h>
#include <iostream>
#include <vector>

using namespace std;

// Complete the commonChild function below.
int commonChild(string s1, string s2) {
    int N = s1.size() + 1;
    // int arr[N][N] = {0,}; // arr로 선언하면 일부 tc에서 segmentation fault 발생
    vector<vector<int>> arr(N, vector<int>(N, 0)); // 벡터는 괜춘 (왜???)
    
    for(int i=1;i<N;i++){
        for(int j=1;j<N;j++){
            if(s1[i-1] == s2[j-1])
                arr[i][j] = arr[i-1][j-1] + 1;
            else 
                arr[i][j] = max(arr[i-1][j], arr[i][j-1]);
        }
    }
    
    return arr[N-1][N-1];
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s1;
    getline(cin, s1);

    string s2;
    getline(cin, s2);

    int result = commonChild(s1, s2);

    fout << result << "\n";

    fout.close();

    return 0;
}
