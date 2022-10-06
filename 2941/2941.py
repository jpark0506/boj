# 특수 알파벳 제거하고 나머지 길이에 더해주는 방식 X
special_alphabet = ["dz=","c=","c-","d-","lj","nj","s=","z="]
cntlist = [0] * len(special_alphabet)
x = input()
x_list = [0] * len(x)
cnt = 0
for alphabets in special_alphabet :
    for i in range(0, len(x)-len(alphabets)+1):
        if x[i:i+len(alphabets)] == alphabets :
            if x_list[i] == 0 :
                cntlist[cnt] += 1
                for j in range(i, i+len(alphabets)):
                    x_list[j] += 1
    cnt += 1
print(sum(cntlist)+len([flag for flag in x_list if flag==0]))