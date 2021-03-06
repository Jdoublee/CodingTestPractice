// 팩토리얼 재귀로 풀기 
// 1년 전에 짠 유물 코드
#include <stdio.h>
int fact(int n){
    if(n<=1)
        return 1;
    else
        return fact(n-1)*n;
}
int main() {
    int n;
    scanf("%d",&n);
    printf("%d\n",fact(n));
    return 0;
}