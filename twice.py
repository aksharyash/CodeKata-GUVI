n=input()
a=input().split()
b=[]
c=0
for i in a:
    c=0
    for j in a:
        if i==j:
            c+=1
        else:
            pass
        if c>=2:
            b.append(i)
print(' '.join([x for x in a if x not in b]))
