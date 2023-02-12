N=int(input())
num_list=list(map(int,input().split()))
M=int(input())
check_list=list(map(int,input().split()))
ans_dict={}
for i in num_list:
    if i in ans_dict:
        ans_dict[i]+=1
    else:
        ans_dict[i]=1
for i in check_list:
    if i in ans_dict:
        print(ans_dict[i],end=' ')
    else:
        print(0,end=' ')