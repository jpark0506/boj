from collections import deque
N,M = map(int, input().split())
data =[]
for _ in range(N):
    li = list(map(int, input()))
    data.append(li)
# data input clear
dst = []
for i in range(N):
    temp = [0] * M
    dst.append(temp)
print(dst)
def bfs(coor):
    queue = deque([coor])
    data[coor[0]][coor[1]] == 0
    dst[0][0]=1
    while queue:
        v = queue.popleft()
        x = v[0]
        y = v[1]
        if x == N-1 and y == M-1 : 
            break
        coordinate = [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]
        for cor in coordinate:
            #좌표 체크
            if cor[0] >= 0 and cor[0] < N and cor[1] >= 0 and cor[1] < M :
                if data[cor[0]][cor[1]]:
                    queue.append([cor[0],cor[1]])
                    data[cor[0]][cor[1]] == 0
                    dst[cor[0]][cor[1]] = dst[x][y]+1
bfs([0,0])
print(dst[N-1][M-1])