# CodingTestPractice
: 코테를 준비합시다 진짜로 (2020. 8. 25. ~ )



##  - 시간초과 방지

1) cpp

```cpp
ios_base :: sync_with_stdio(false);
cin.tie(NULL);
cout.tie(NULL);
// 코드 앞에 추가
```

2) python3

```python
import sys
n = sys.stdin.readline().rstrip() # rstrip() 잊지말기^^77
# input() 대신 사용
# input = sys.stdin.readline 꼴로 선언 후 input().rstrip() 사용 가능

```



## - 런타임에러 방지

1) python3

```python
import sys
sys.setrecursionlimit(10**6)
# 파이썬이 정한 최대 재귀 깊이를 변경해줌
# 기본 1000 -> 10000 or 10**6 정도로 변경
# 재귀 함수 사용할 때 (예:dfs)
```





##  - dfs/bfs 차이

> 탐색 범위가 넓은 경우와 전체 탐색을 하지 않아도 될 경우는 bfs를 이용하고 ,
>
> 전체 탐색이 필요하거나 순차적으로 찾을 필요가 있는 경우는 dfs를 사용하는 것이 좋다.

- **bfs를 이용하는 경우**

1. 시작 지점에서 가장 가까운 것을 구하고 싶은 경우

2. 탐색 범위 자체는 넓지만 어느정도 근처에 구하고 싶은 해가 존재하는 것을 알고 있는 경우

3. 탐색 범위가 굉장히 넒으며 dfs를 사용할 때 스택이 대량으로 사용될 경우



- **dfs를 이용하는 경우**

1. 모든 경로를 탐색하고 결과를 확인해야 하는 경우

2. 문자열 등을 탐색할 때 '사전 순서로 앞에오는 것'처럼 앞에서 검색해서 찾는 것이 빠를 경우





## 0) 현실적이고 직관적인 공부 순서

1~3번만 제대로 하면 된다. 4번은 추가적으로 공부.

1. **그리디 알고리즘부터 풀기**

   - 가장 쉬운 개념의 알고리즘

   - 많이 출제됨

2. **탐색 - DFS, BFS**

3. **기본 동적 프로그래밍**

4. 그래프 이론, 중급 및 고급 동적 프로그래밍, 문자열

   

**\* ~~코드업 기초 100제~~** 풀고 **1~3번 50문제씩** 풀기

## 1) 백준

### - [단계별로 풀어보기](https://www.acmicpc.net/step)

- 재귀, 정렬, 브루트 포스, 그리디알고리즘, 스택, 이분탐색, DFS, BFS, 구현, 다이나믹프로그래밍

### - 백준 dfs문제 풀 때 주의사항

- 아래 세 줄 필수 -> **시간 초과 / 런타임 에러** 발생 방지

```python
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
```



## 2) 알고리즘문제해결전략

### -[1-8, 10, 14, 16-19, 21-25, 27-32]



## 3) 프로그래머스

### - [모든 문제](https://programmers.co.kr/learn/challenges?tab=all_challenges)



## 4) SQL

### - Programmers, HackerRank
