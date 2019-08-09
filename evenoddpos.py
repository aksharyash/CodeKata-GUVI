n=int(input())
inp=list(input().split())
for i in range(len(inp)):
    if i%2!=0:
        if int(inp[i])%2==0:
            print(inp[i],end=' ')
    elif i%2==0:
        if int(inp[i])%2!=0:
            print(inp[i],end=' ')
