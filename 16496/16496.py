from functools import cmp_to_key
N = int(input())
data = list(map(str, input().split()))
data.sort(reverse=True)
def custom_sort(a,b):
    return int(b+a) - int(a+b)
data2 = sorted(data, key=cmp_to_key(custom_sort))
answer = ''
for d in data2 :
    answer += d
if answer[0] == '0' :
    print("0")
else : 
    print(answer)