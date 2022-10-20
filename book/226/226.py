N,M = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input()))
INF = int(1e9)
d = [INF] * (M+max(coin)+1)
d[0] = 0
for i in range(M):
    for c in coin:
        d[i+c] = min(d[i]+1, d[i+c])
if d[M] == INF : 
    print(-1)
else:
    print(d[M])

print("DP 테이블 :")
print(d)
    
