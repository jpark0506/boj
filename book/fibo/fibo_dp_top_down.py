#피보나치 수열이란
#f(An) = f(An-1) + f(An-2)
#dp를 이용한 시간 줄이기


d = [0] * 100
#dp fibo
#top down 방식
def fibo(x):
    print(str(x) + " 호출")
    if x == 1 or x == 2:
        return 1
    elif d[x] != 0:
        return d[x]
    d[x] = fibo(x-1)+ fibo(x-2)
    return d[x]
print(fibo(99))