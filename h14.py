from itertools import permutations
n=list(map(str,input()))
lst=[]
per=list(permutations(n,len(n)))
for i in per:
    lst.append("".join(i))
lst=set(lst)
for i in lst:
    print(i)
        
