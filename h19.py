h,x=map(int,input().split())
lst=[]
my=[]
for i in range(h):
    a=input().split()
    b=set(a)
    for i in b:
        lst.append(i)
for i in lst:
    if lst.count(i)==h:
        my.append(i)
print(' '.join(set(sorted(my))))
