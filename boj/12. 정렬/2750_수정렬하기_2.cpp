// sort 대신 정렬 구현
#include <iostream>
#include <algorithm>
using namespace std;
// 버블정렬 구현
void bubbleSort(int arr[],int n){ 
    for(int i=n-1;i>0;i--){
        for(int j=0;j<i;j++){
            if(arr[j]>arr[j+1])
                swap(arr[j],arr[j+1]); // <algorithm> header에 존재
        }
    }
}
int main() {
	int n;
	cin>>n;
	int arr[n];
	for(int i=0;i<n;i++)
		cin>>arr[i];
	bubbleSort(arr,n);
	for(int i=0;i<n;i++)
		cout<<arr[i]<<"\n";
	return 0;
}