h,x=map(int,input().split())
lst=[]
my=[]
for i in range(h):
    a=input().split()
    for i in a:
        lst.append(i)
for i in lst:
    if lst.count(i)>=h:
        my.append(i)
print(' '.join(set(sorted(my))))
