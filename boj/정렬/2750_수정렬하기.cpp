// sort 대신 정렬 구현
#include <iostream>
using namespace std;

int main() {
	int n;
	cin>>n;
	int arr[n];
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
    // 삽입정렬 구현
	for(int i=1;i<n;i++){
		int key=arr[i]; // key값은 두 번째 원소부터
		int j=i-1; // key 앞의 원소들은 이미 정렬되어 있음
		while(j>=0&&arr[j]>key){ // key 보다 큰 값 있다면 뒤로 한 칸 이동
			arr[j+1]=arr[j];
			j--;
		}
		arr[j+1]=key; // 빈 공간에 key 넣어줌
	}
	
	for(int i=0;i<n;i++)
		cout<<arr[i]<<"\n";
	return 0;
}