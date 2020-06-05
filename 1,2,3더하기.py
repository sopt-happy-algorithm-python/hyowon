import sys
from itertools import product as c
a=int(sys.stdin.readline())
p=[1,2,3]
for i in range(a):
    count=0
    r=[]
    b=int(sys.stdin.readline())
    for j in range(1,b+1):
        result=list(c(p,repeat=j))
        r.extend(result)
    for j in range(len(r)):
        if sum(r[j])==b:
            count+=1
    print(count)
