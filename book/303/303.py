from collections import deque
import copy
n = int(input())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)
for i in range(n):
    li = list(map(int, input()))
    time = li[0]
    subject_list= li[1:-1]
    for x in subject_list:
        indegree[i+1] += 1
        graph[x].append(i+1)
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i]-=1
            if indegree[i]==0 :
                q.append(i)
    for i in range(1,n+1):
        print(result[i])

topology_sort()



