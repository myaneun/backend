from collections import deque
import sys
input = sys.stdin.readline

N,M,V = map(int, input().split())
graph = [[False]*(N+1) for _ in range(N+1)]

##간선
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
    
visited1 = [False]*(N+1) ##dfs 방문기록
visited2 = [False]*(N+1) ##bfs 방문기록

def DFS(v):
    visited1[v] = True
    print(v, end=' ')
    for i in range(1, N+1):
        if graph[v][i] and (not visited1[i]):
            DFS(i)

def BFS(v):
    q = deque([v])
    visited2[v]=True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, N+1):
            if graph[v][i] and (not visited2[i]):
                q.append(i)
                visited2[i] = True

DFS(V)
print()
BFS(V)