INF = int(1e9)

v = int(input())
e = int(input())

graph = [[INF]*(v+1) for i in range(v+1)]
for i in range(v+1):
    graph[i][i] = 0
for _ in range(e):
    a,b,c = input().split()
    graph[a][b] = c
for k in range(v+1):
    for a in range(v+1):
        for b in range(v+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
for a in range(v+1):
    for b in range(v+1):
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()

