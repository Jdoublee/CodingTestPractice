// 맨 처음에 주어진 변수명 그대로 썼다.
// BFS 문제
// c++, java 밖에 제공 안 되서 씨쁠쁠로 구현
#include <vector>
#include <queue>

using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    
    int x, y;
    int dx[] = {-1, 0, 0, 1};
    int dy[] = {0, -1, 1, 0};
    
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(picture[i][j] > 0){
                number_of_area++;
                int cnt = 1;
                queue<pair<int,int>> q;
                
                q.push(make_pair(i,j));
                int now = picture[i][j];
                picture[i][j] = 0;
                
                while(!q.empty()){
                    x = q.front().first;
                    y = q.front().second;
                    q.pop();
                    
                    for(int k=0;k<4;k++){
                        int nx = x + dx[k];
                        int ny = y + dy[k];
                        
                        if(nx >= 0 && nx < m && ny >=0 && ny < n && picture[nx][ny] == now){
                            q.push(make_pair(nx,ny));
                            picture[nx][ny] = 0;
                            cnt++;
                        }
                    }
                }
                max_size_of_one_area = max(max_size_of_one_area, cnt);
            }
        }
    }
    
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    
    return answer;
}