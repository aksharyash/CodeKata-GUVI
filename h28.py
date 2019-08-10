n=list(input())
str=''
for i in n:
    if i not in str:
        print(i,end='')
        str=str+i
    else:
        str=str+i
