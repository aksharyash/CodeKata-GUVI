n=int(input())
inp=list(input().split())
str=""
lst=[]
for i in inp:
    if i in str:
        lst.append(i)
        break
    else:
        str=str+i
if lst==[]:
    print("unique")
else:
    print(''.join(lst))
    
    
  
