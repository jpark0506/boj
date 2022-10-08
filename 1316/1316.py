N = int(input())
# 같을 때, 통과
# 다를 때 이전 단어 리스트에 있었는지 확인하고 
# 있으면 그룹 단어 실패
# 아니면 그룹 단어 아님, 리스트 추가
cnt = 0
for i in range(N):
    M = input()
    letter_list = [M[0]]
    flag = True
    for j in range(len(M)-1):
        if M[j] != M[j+1]:
            inner_flag = True
            
            for k in letter_list:
                if M[j+1] == k:
                    inner_flag = False
                    break
            if inner_flag == False:
                flag = False
                break
            else:
                letter_list.append(M[j+1])
        else:
            letter_list
    if flag:
        cnt += 1
print(cnt)