n=int(input())
inp=list(map(int,input().split()))
lst=[[inp[i],inp[j],inp[k]] for i in range(len(inp)) for j in range(len(inp)) for k in range(len(inp))if inp[i]+inp[j]==inp[k] and inp[i]<inp[j]<inp[k]]
for i in lst:
    for j in i:
        if j=='[' or j==']' or j==',':
            pass
        else:
            print(j,end=' ')
    print()
