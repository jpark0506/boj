# BFS의 동작 과정
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다. 
# 2. 큐에서 노드를 꺼내 해단 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다
# 3. 2번의 과정이 더 이상 수행될 수 없을 때까지 반복
# 구현 방법
# 큐!
from collections import deque
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,4],
    [3,5],
    [7],
    [2,6,8],
    [1,7]
]
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * 9
bfs(graph,1, visited)