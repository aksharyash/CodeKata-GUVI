n=int(input())
lst=[x for x in input().split()]
arr=[]
c=0
for i in lst:
    if int(i)==c:
        arr.append(i)
    c+=1
if arr==[]:
    print(-1)
else:
    print(' '.join(sorted(arr))) 
