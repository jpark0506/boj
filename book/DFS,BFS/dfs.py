# DFS의 동작 과정
# 1. 탐색 시작 노드를 스택에 삽입 후 방문 처리
# 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 쌓고 방문 처리를 해준다
# 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다
# 3. 2번이 더 이상 수행될 수 없을 때까지 반복한다

# 구현 방법 :
# 재귀 호출을 이용한 구현 방법이 일반적임

# DFS의 구성 요소
# - 방문 배열, 그래프(구현 방법 생각), 현재 노드
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end =' ')
    for i in graph[v]:
        if not visited[v]:
            dfs(graph, i, visited)
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
visited = [False] * 9
dfs(graph, 1, visited)
