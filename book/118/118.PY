N, M = map(int, input().split())
A,B,d = map(int, input().split())
data = []
for _ in range(M):
    temp_list = list(map(int,input().split()))
    data.append(temp_list)
# print(li)
#입력 완료
# 0 N, 1 E, 2 S, 3 W
#넘 비효율적 구현...;;
#아직 파이썬 피지컬(?)[책에 나와 있던 용어]이 많이 부족함
data2 = []
for i in range(M+2):
    temp = []
    for j in range(N+2):
        if i == 0 or i == M+1 or j == 0 or j == N+1:
            temp.append(-1)
        else:
            temp.append(0)
    data2.append(temp)
for i in range(M):
    for j in range(N):
        if data[i][j] == 0:
            data2[i+1][j+1] = -1
direction = [[-1, 0],[0,1],[1,0],[0,-1]]
cur_pos = [A+1,B+1]
def sub_left(cur_pos,dir):
    return [cur_pos[0]-direction[dir][0],cur_pos[1]-direction[dir][0]]
left_pos = sub_left(cur_pos,d)
while True:
    if sub_left()