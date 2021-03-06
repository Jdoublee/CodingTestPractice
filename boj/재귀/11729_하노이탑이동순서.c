// 하노이탑 문제
// 오랜만에 다시 보니 반갑당
// 단골 개념이었지
#include <stdio.h>
int count=0;
void hanoi(int s,int m,int d,int n){
    count++;
    if(n==1)
        return;
    else{
        hanoi(s,d,m,n-1);
        hanoi(m,s,d,n-1);
    }
}
void print_hanoi(int s,int m,int d,int n){
    if(n==1)
        printf("%d %d\n",s,d);
    else{
        print_hanoi(s,d,m,n-1);
        printf("%d %d\n",s,d);
        print_hanoi(m,s,d,n-1);
    }
}
int main() {
    int n;
    scanf("%d",&n);
    
    hanoi(1,2,3,n);
    printf("%d\n",count);
    print_hanoi(1,2,3,n);
    
    return 0;
}
