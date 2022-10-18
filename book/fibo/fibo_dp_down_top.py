#down_top 방식
d = [0] * 100000

N = int(input())
d[1] = 1
d[2] = 1

for i in range(3,N+1):
    if d[i] == 0:
        d[i]= d[i-1]+d[i-2]

print(d[N])