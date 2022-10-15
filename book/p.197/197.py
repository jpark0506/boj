N = int(input())
store_data = list(map(int,input().split()))
M = int(input())
customer_data = list(map(int,input().split()))
def binary_search(array, target, start,end) :
    while start <= end:
        if start > end: 
            return None
        mid = (start + end)//2
        if array[mid] == target : 
            return mid
        elif array[mid] > target :
            end = mid - 1
        else:
            start = mid + 1

for data in customer_data :
    if binary_search(store_data, data, 0, N-1) != None:
        print("yes", end = " ")
    else:
        print("no", end = " ")