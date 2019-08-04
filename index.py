n=int(input())
lst=[x for x in input().split()]
arr=[]
c=0
for i in lst:
    if int(i)==c:
        arr.append(i)
    c+=1
print(' '.join(sorted(arr)))   
