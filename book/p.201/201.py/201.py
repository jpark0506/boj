N,M = map(int,input().split()) 
input_data = list(map(int, input().split()))

start = 0
end = max(input_data)

while start <= end :
    total = 0
    mid = (start+end) // 2
    for i in input_data:
        if i > mid:
            total += i- mid
    if total < M:
        end = mid - 1
    else : 
        result = mid
        start = mid + 1
print(result)