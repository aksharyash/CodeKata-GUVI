n=input()
a=input()
l=[]
for i in a:
    c=0
    for j in a:
        if i==j:
            c+=1
            if c>=2:
                l.append(j)
                c=0
        else:
            pass
print(sorted(set(''.join(l))))
    
    
  
