import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
N,M,C = map(int, input().split())
distance = [INF*30001]
distance[C] = 0
graph = [[] for i in range(N+1)]
for _ in range(M):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))

def d(start):
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
d(C)