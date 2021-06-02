// 너무 더러운데 완탐이니 이렇게 해도 되겠지....?
// 문제를 잘 읽자
#include <string>
#include <vector>

using namespace std;
bool check(vector<vector<int>> v, int m, int n){
    int tot=0;
    int len=v.size();
    // 자물쇠 영역 내부만 확인
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            // 자물쇠 영역 내에서는 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 조건때문에 추가 (테케 23,25,33 실패 해결)
            if(v[m-1+i][m-1+j]>1)
                return false;
            tot+=v[m-1+i][m-1+j];
        }
    }
    if(tot==n*n)
        return true; // 홈 다 채웠음
    else
        return false;
}
bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
    bool answer = false;
    int m = key.size();
    int n = lock.size();
    if(check(lock,m,n))
        return true;
    
    for(int i=0;i<4;i++){
        if(i>0){ // 90도 회전
            vector<vector<int>> kk = key;
            for(int j=0;j<m;j++){
                for(int k=0;k<m;k++){
                    key[k][m-1-j]=kk[j][k];
                }
            }
        }
        // 2*m+n-2 크기의 이동&비교용 배열 v 생성
        vector<vector<int>> v(2*m+n-2, vector<int>(2*m+n-2, 1));
        for(int j=0;j<n;j++){
            for(int k=0;k<n;k++){
                if (lock[j][k]==0)
                    v[m-1+j][m-1+k]=lock[j][k];
            }
        }
        // v에서 key 이동해가며 비교
        vector<vector<int>> vtmp; // 비교 위해 v 값 동일하게 저장할 벡터 선언
        for(int j=0;j<n+m-1;j++){
            for(int k=0;k<n+m-1;k++){
                vtmp = v;
                for(int a=0;a<m;a++){
                    for(int b=0;b<m;b++){
                        vtmp[j+a][k+b]+=key[a][b]; // 0+0 / 0+1 / 1+1
                     }
                 }
                if(check(vtmp,m,n))
                    return true;
            }
        }   
    return answer;
}