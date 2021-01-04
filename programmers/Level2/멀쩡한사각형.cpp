using namespace std;

long long solution(int w,int h) {
    long long answer = 0;
    
    for(long long i = 1; i < w; i++){
        answer += (h * i) / w;
    }
    
    return answer * 2;
}
