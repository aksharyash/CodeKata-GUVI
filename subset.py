a,b=list(map(int,input().split()))
c=list(map(str,input().split()))
d=list(map(str,input().split()))
p=0
for i in range(len(d)):
        if d[i] in c:
            p+=1
            continue
if p==len(d):
    print("YES")
else:
    print("NO")
