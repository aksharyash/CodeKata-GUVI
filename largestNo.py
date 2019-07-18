n=input()
a=input().split()
a=(list(sorted((a))))
b=a[::-1]
if b[0]=='0':
    print("0")
else:
    print("".join(b))
  
