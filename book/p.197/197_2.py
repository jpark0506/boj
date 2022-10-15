n= int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] += 1

m = int(input())
input_data = list(map(int, input().split()))

for data in input_data:
    if array[data] > 0:
        print("yes", end=" ")
    else:
        print("no", end=" ")