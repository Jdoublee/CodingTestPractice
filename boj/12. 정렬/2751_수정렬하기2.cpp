// sort 대신 정렬 구현
// nlogn
#include <iostream>
#include <algorithm>
using namespace std;
int sorted[1000000]; // 정렬된 원소 저장할 임시 배열
// merge sort 구현
void merge(int arr[],int l,int m,int r){
    // i : 정렬된 왼쪽 리스트에 대한 인덱스
    // j : 정렬된 오른쪽 리스트에 대한 인덱스
    // k : 정렬될 리스트에 대한 인덱스
    int i=l,j=m+1;
    int k=l;
    //합병
    while(i<=m&&j<=r){
        if(arr[i]<=arr[j])
            sorted[k++]=arr[i++];
        else
            sorted[k++]=arr[j++];
    }
    //합병후 남은 값들 뒤에 다 붙여줌
    if(i>m)
        for(int n=j;n<=r;n++)
            sorted[k++]=arr[n];
    else
        for(int n=i;n<=m;n++)
            sorted[k++]=arr[n];
    //원래 arr에 정렬된 배열 다시 복사
    for(int n=l;n<=r;n++)
        arr[n]=sorted[n];
}
void mergeSort(int arr[],int l,int r){
    if(l<r){
        int m=(l+r)/2; // divide
        mergeSort(arr,l,m); // conquer
        mergeSort(arr,m+1,r); // conquer
        merge(arr,l,m,r); // combine
    }
}
int main() {
	int n;
	cin>>n;
	int arr[n];
	for(int i=0;i<n;i++)
		cin>>arr[i];
	mergeSort(arr,0,n-1);
	for(int i=0;i<n;i++)
		cout<<arr[i]<<"\n";
	return 0;
}