I = str(input())
a = int(ord(I[0])-ord('a'))+1
b = int(I[1])
# dxdy 선언 중요

move_dir = [(-2,-1),(-1,-2),(2,1),(1,2),(-1,2),(2,-1),(1,-2),(-2,1)]
cnt = 8
for cmd in move_dir:
    move_result = (cmd[0]+a,cmd[1]+b)
    if move_result[0] > 8 or move_result[0] < 1:
        cnt -= 1
    elif move_result[1] > 8 or move_result[1] < 1:
        cnt -=1
print(cnt)