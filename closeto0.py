from itertools import permutations
n=int(input())
my=[]
lst=list(map(int,input().split()))
per=list(permutations(lst,2))
for i in per:
    if sum(i[:])==0:
        print(str(i[0])+" "+str(i[1]))
        break
