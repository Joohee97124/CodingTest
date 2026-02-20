import sys
from collections import deque

input = sys.stdin.readline

def solve():
    # 1. 입력 받기
    n = int(input())  
    v = int(input())  
    
    # 2. 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for _ in range(v):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)  

    # 3. 방문 체크 및 큐 세팅
    visited = [False] * (n + 1)
    que = deque([1])  
    visited[1] = True
    count = 0
    
    # 4. BFS 탐색
    while que:
        curr = que.popleft()
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True 
                que.append(neighbor)     
                count += 1
                
    # 5. 결과 출력
    print(count)

solve()