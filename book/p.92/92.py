N,M,K = map(int,input().split())
data = list(map(int,input().split()))
data.sort()
first = data[N-1]
second = data[N-2]
data2 = [first for i in range(K)]
data2.append(second)
print(data2)
print(sum(data2)*(M//(K+1))+ sum(data2[:(M%(K+1))]))