#음료수 얼려 먹기
N,M = map(int, input().split())
data = []
for i in range(N):
    temp = list(map(int, input()))
    data.append(temp)
# input process clear
# 내 두번째 고민 어떻게 하면 그래프로 표현할 수 있는가?
# data를 visited 그래프로 보면 되지 않을까?
# 모든 방문하지 않은 dfs하는 방식
def dfs(X,Y):
    if X<0 or Y<0 or X> N-1 or Y>M-1:
        return False
    if data[X][Y]:
        return False
    
    data[X][Y] = 1
    
    dfs(X+1,Y)
    dfs(X,Y+1)
    dfs(X-1,Y)
    dfs(X,Y-1)

    return True
        
#python은 0 빼고 True

answer = 0
for i in range(N):
    for j in range(M):
        if not data[i][j]:
            if dfs(i,j):
                answer += 1
print(answer)